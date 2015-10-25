import argparse
import logging
import os
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

import sesamecontract.util.logging as logutil

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("file", help="File to encrypt")
    parser.add_argument("-t", "--time",
        help="The datetime after which the file can be decrypted")
    return parser.parse_args()

def main():
    logutil.set_stream_handler(logger)
    args = parse_args()
    infile = open(args.file, "rb")
    outfile = open(args.file + ".sesame", "wb")
    outfile.write(b"=== Sesame ===\n")
    outfile.write(b"ver: 0.1\n")
    backend = default_backend()
    key = os.urandom(32)
    iv = os.urandom(12)
    outfile.write(b"iv: " + b64encode(iv) + b"\n")
    outfile.write(b"key: " + b64encode(key) + b"\n")
    outfile.write(b"===\n")
    cipher = Cipher(algorithms.AES(key), modes.GCM(iv), backend=backend)
    encryptor = cipher.encryptor()
    while True:
        data = infile.read(4096)
        if not data:
            break
        outfile.write(encryptor.update(data))
    outfile.write(encryptor.finalize())
    infile.close()
    outfile.close()

if __name__ == '__main__':
    main()
