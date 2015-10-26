import argparse
import logging

import sesamecontract.util.logging as logutil
from sesamecontract.crypto import SesameCrypto

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

    crypto = SesameCrypto()
    with open(args.file, "rb") as infile:
        with open(args.file + ".sesame", "wb") as outfile:
            outfile.write(b"=== Sesame ===\n")
            outfile.write(b"ver: 0.1\n")
            outfile.write(b"iv: " + crypto.get_iv() + b"\n")
            outfile.write(b"key: " + crypto.get_key() + b"\n")
            outfile.write(b"===\n")
            crypto.encrypt(infile, outfile)

if __name__ == '__main__':
    main()
