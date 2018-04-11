import unittest
from app.base64 import Base64

class test_Base64(unittest.TestCase):
    

    def test_encode_man(self):
        m = Base64
        self.assertEqual(m.encode("Man"),"TWFu")

    def test_encode_a(self):
        m = Base64
        self.assertEqual(m.encode("a"),"YQ==")
    

    def test_decode_man(self):
        m = Base64
        self.assertEqual(m.decode("TWFu"),"Man")

    def test_decode_a(self):
        m = Base64
        self.assertEqual(m.decode("YQ=="),"a")

