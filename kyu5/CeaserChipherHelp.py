"""DESCRIPTION:
Write a class that, when given a string, will return an uppercase string with each letter shifted forward in the alphabet by however many spots the cipher was initialized to.

For example:

c = CaesarCipher(5); # creates a CipherHelper with a shift of five
c.encode('Codewars') # returns 'HTIJBFWX'
c.decode('BFKKQJX') # returns 'WAFFLES'
If something in the string is not in the alphabet (e.g. punctuation, spaces), simply leave it as is.
The shift will always be in range of [1, 26].
"""

class CaesarCipher(object):
    def __init__(self, shift):
        self.alph ='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.key = {}
        for i in range(len(self.alph)):
            self.key[self.alph[i]] = self.alph[((i + shift) % 26)]
        pass
    def encode(self, st):
        list = []
        for i in st.upper():
            if i not in self.alph:
                list.append(i)
            else:
                list.append(self.key[i])
        return ''.join(list)
        pass

    def decode(self, st):
        list = []
        for i in st.upper():
            if i not in self.alph:
                list.append(i)
            else:
                for j in self.alph:
                    if self.key[j] == i:
                        list.append(j)
        return ''.join(list)
