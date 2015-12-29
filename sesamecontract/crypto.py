import os
from base64 import b64encode
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

class SesameCrypto():
    """
    Helper class that wraps the cryptography AES functions
    """

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

def retrieve_key(points, k):
    """
    Given points constructed from Shamir's secret sharing algorithm, recovers
    the original 16-byte key
    """
    if len(points) < k:
        raise ValueError("Not enough points to reconstruct key")

    # prime used to define finite field
    p = 275990457285843570502088317104276687707

    # straightforward implementation of Lagrange basis evaluation
    a0 = 0
    for point in points:
        x, y = point
        num = y
        denom = 1
        for pi in points:
            xi = pi[0]
            if xi == x:
                continue
            num *= -xi
            denom *= x - xi
        a0 = (a0 + num//denom) % p

    key = a0.to_bytes(16, byteorder='little')

    return key

def split_key(key, k, n):
    """
    Uses Shamir's secret sharing algorithm to split a 16-byte key into n points
    with k threshold
    """

    if len(key) != 16:
        raise ValueError("Key must be 16 bytes")
    if k > n:
        raise ValueError("Threshold should not be greater than number of points")

    # interpret int from bytes
    convert_int = lambda s: int.from_bytes(s, byteorder='little')

    # prime used to define finite field
    p = 275990457285843570502088317104276687707

    # uniformly-distributed generation of number [0, p)
    def generate_int():
        while True:
            num = convert_int(os.urandom(16))
            if num < p:
                return num

    # generate k polynomial coefficients
    coefficients = [convert_int(key)]
    coefficients += [generate_int() for _ in range(k-1)]
    print("coefficients:", coefficients)

    # horner's method to evaluate polynomial
    def horner(x):
        result = 0
        for i in reversed(range(k)):
            result = (result * x + coefficients[i]) % p
        return result

    # generate n points
    points = [(x, horner(x)) for x in range(1, n+1)]

    return points
