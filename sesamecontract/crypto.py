import os
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class SesameCrypto():

    def __init__(self):
        self.key = os.urandom(32)
        self.iv = os.urandom(12)
        self.backend = default_backend()

    def get_key(self):
        return b64encode(self.key)

    def get_iv(self):
        return b64encode(self.iv)

    def encrypt(self, infile, outfile):
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(self.iv), backend=self.backend)
        encryptor = cipher.encryptor()
        while True:
            data = infile.read(4096)
            if not data:
                break
            outfile.write(encryptor.update(data))
        outfile.write(encryptor.finalize())
