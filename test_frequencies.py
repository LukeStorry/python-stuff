
import unittest
from app.frequencies import Frequencies

class test_CalculateFrequencies(unittest.TestCase):

###

    def test_countLetters_blank(self):
        f = Frequencies()
        self.assertEqual(f.countLetters(""), {})

    def test_countLetters_a(self):
        f = Frequencies()
        self.assertEqual(f.countLetters("a"), {"a": 1})

    def test_countLetters_ab(self):
        f = Frequencies()
        self.assertEqual(f.countLetters("ab"), {"a": 1, "b": 1})

    def test_countLetters_abb(self):
        f = Frequencies()
        self.assertEqual(f.countLetters("abb"), {"a": 1, "b": 2})

###


    def test_countPairs_blank(self):
        f = Frequencies()
        self.assertEqual(f.countPairs(""), {})

    def test_countPairs_a(self):
        f = Frequencies()
        self.assertEqual(f.countPairs("aa"), {"aa": 1})

    def test_countPairs_aab(self):
        f = Frequencies()
        self.assertEqual(f.countPairs("aab"), {"aa": 1, "ab": 1})

    def test_countPairs_aaab(self):
        f = Frequencies()
        self.assertEqual(f.countPairs("aaab"), {"aa": 2, "ab": 1})


###


    def test_countTriplets_blank(self):
        f = Frequencies()
        self.assertEqual(f.countTriplets(""), {})

    def test_countTriplets_aaa(self):
        f = Frequencies()
        self.assertEqual(f.countTriplets("aaa"), {"aaa": 1})

    def test_countTriplets_aaab(self):
        f = Frequencies()
        self.assertEqual(f.countTriplets("aaab"), {"aaa": 1, "aab": 1})

    def test_countTriplets_aaaabb(self):
        f = Frequencies()
        self.assertEqual(f.countTriplets("aaaabb"), {"aaa": 2, "aab": 1, "abb": 1})



###

    def test_dictToSStr_blank(self):
        f = Frequencies()
        self.assertEqual(f.dictToSStr({}), "")

    def test_dictToSStr_a1(self):
        f = Frequencies()
        self.assertEqual(f.dictToSStr({"a":1}), "a:1 ")

    def test_dictToSStr_a1b1(self):
        f = Frequencies()
        self.assertEqual(f.dictToSStr({"a":1, "b":1}), "a:1 b:1 ")

    def test_dictToSStr_a2b1(self):
        f = Frequencies()
        self.assertEqual(f.dictToSStr({"a":2, "b":1}), "a:2 b:1 ")

    def test_dictToSStr_a1b2(self):
        f = Frequencies()
        self.assertEqual(f.dictToSStr({"a":1, "b":2}), "b:2 a:1 ")

###
    def test_topTen_blank(self):
        f = Frequencies()
        self.assertEqual(f.topTen(""), "Letters: \nPairs: \nTriplets: \n")

    def test_topTen_a(self):
        f = Frequencies()
        self.assertEqual(f.topTen("a"), "Letters: a:1 \nPairs: \nTriplets: \n")

    def test_topTen_ab(self):
        f = Frequencies()
        self.assertEqual(f.topTen("ab"), "Letters: a:1 b:1 \nPairs: ab:1 \nTriplets: \n")

    def test_topTen_aaa(self):
        f = Frequencies()
        self.assertEqual(f.topTen("aaa"), "Letters: a:3 \nPairs: aa:2 \nTriplets: aaa:1 \n")

###
