import unittest
import os

from sesamecontract import crypto

class TestSecretSplit(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.keys = [b'0123456789abcdef',
                     bytes(range(16)),
                     bytes(range(255, 255-16, -1)),
                     b''.join(b'\xff' for _ in range(16)),
                     b''.join(b'\x00' for _ in range(16))]

    def generate_key(self):
        return os.urandom(16)

    def test_split(self):
        for key in self.keys:
            points = crypto.split_key(key, n=5, k=5)
            self.assertEqual(len(points), 5)

        for key in self.keys:
            points = crypto.split_key(key, n=3, k=1)
            self.assertEqual(len(points), 3)

        with self.assertRaises(Exception):
            crypto.split_key(self.keys[0], n=1, k=2)

    def test_retrieve(self):
        for key in self.keys:
            points = crypto.split_key(key, n=5, k=5)
            reconstruction = crypto.retrieve_key(points)
            self.assertEqual(key, reconstruction)

            points = crypto.split_key(key, n=5, k=3)
            reconstruction = crypto.retrieve_key(points[:3])
            self.assertEqual(key, reconstruction)

            points = crypto.split_key(key, n=5, k=1)
            reconstruction = crypto.retrieve_key(points[:1])
            self.assertEqual(key, reconstruction)

    def test_random_keys(self):
        for _ in range(100):
            key = self.generate_key()
            points = crypto.split_key(key, n=5, k=3)
            reconstruction = crypto.retrieve_key(points[:3])
            self.assertEqual(key, reconstruction)
