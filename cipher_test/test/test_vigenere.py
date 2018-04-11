import unittest
from app.vigenere import Vigenere

class test_Vigenere(unittest.TestCase):
    
    def test_encode_blank(self):
        m = Vigenere
        self.assertEqual(m.encode("a","abc"),"abc")
    
    def test_encode_abc(self):
        m = Vigenere
        self.assertEqual(m.encode("abc","abc"),"def")


    def test_encode_example(self):
        m = Vigenere
        self.assertEqual(m.encode("BRISTOL","MEETMEATMIDNIGHTBYTHEBRIDGE"),"NVMLFSLUDQVGWRIKJQMVPCIQVZS")



    def test_decode_blank(self):
        m = Vigenere
        self.assertEqual(m.decode("a","abc"),"abc")

    def test_decode_abc(self):
        m = Vigenere
        self.assertEqual(m.decode("abd","def"),"abc")

    def test_decode_example(self):
        m = Vigenere
        self.assertEqual(m.decode("BRISTOL","NVMLFSLUDQVGWRIKJQMVPCIQVZS"),"MEETMEATMIDNIGHTBYTHEBRIDGE")
