class Monoalphabetic:
    code = {"": ""}

    def __init__(self, key):
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        key = key.upper()
        for char in alphabet:
            if char not in key:
                key += char
        for i in range(len(key)):
            self.code[alphabet[i]] = key[i]

    def encode(self, text):
        result = ""
        for char in text.upper():
            result += self.code[char]
        return result

    def decode(self, text):
        result = ""
        for char in text.upper():
            for key in self.code:
                if self.code[key] == char:
                    result += key
        return result

m = Monoalphabetic("key")
