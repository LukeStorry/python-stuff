class Frequencies:

    def countLetters(self, s):
        count = {}
        for letter in s:
            count[letter] = count.get(letter, 0) + 1
        return count

    def countPairs(self, s):
        count = {}
        for i in range(len(s) - 1):
            pair = s[i] + s[i + 1]
            count[pair] = count.get(pair, 0) + 1
        return count

    def countTriplets(self, s):
        count = {}
        for i in range(len(s) - 2):
            triplet = s[i] + s[i + 1] + s[i + 2]
            count[triplet] = count.get(triplet, 0) + 1
        return count

    def dictToSStr(self,d):
        s=""
        for key in sorted(d,key=d.__getitem__, reverse=True):
            s+= "%s:%d " %(key, d[key])
        return s

    def topTen(self, s):
        output = ""
        output+="Letters: " + self.dictToSStr(self.countLetters(s)) + "\n"
        output+="Pairs: " + self.dictToSStr(self.countPairs(s)) + "\n"
        output+="Triplets: " + self.dictToSStr(self.countTriplets(s)) +"\n"
        return output

if __name__ == '__main__':
    import os,sys
    input = sys.argv[1]
    f = Frequencies()
    print f.topTen(input)
