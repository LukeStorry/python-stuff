import unittest
from app.monoalphabetic import Monoalphabetic


class test_Monoalphabetic(unittest.TestCase):

    def test_encode_blank(self):
        m = Monoalphabetic("")
        self.assertEqual(m.encode("abc"), "ABC")

    def test_encode_abc(self):
        m = Monoalphabetic("a")
        self.assertEqual(m.encode("abc"), "ABC")

    def test_encode_zab(self):
        m = Monoalphabetic("z")
        self.assertEqual(m.encode("abc"), "ZAB")

    def test_decode_blank(self):
        m = Monoalphabetic("")
        self.assertEqual(m.decode("abc"), "ABC")

    def test_decode_abc(self):
        m = Monoalphabetic("a")
        self.assertEqual(m.decode("abc"), "ABC")

    def test_decode_zab(self):
        m = Monoalphabetic("z")
        self.assertEqual(m.decode("zab"), "ABC")
