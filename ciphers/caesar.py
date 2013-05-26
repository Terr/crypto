import string

from base import SubstitutionCipher


class CaesarCipher(SubstitutionCipher):
    def encrypt(self, text):
        if not self.shift:
            raise Exception('shift property is not set or 0')

        return self.shift_text(text, self.shift)

    def decrypt(self, text):
        if not self.shift:
            raise Exception('shift property is not set or 0')

        return self.shift_text(text, self.shift * -1)
