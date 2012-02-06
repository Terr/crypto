import string

from base import SubstitutionCipher
from decorators import uppercase_text


class CaesarCipher(SubstitutionCipher):
    def __init__(self, shift=None):
        """Initialize cipher with optional `shift`.

        `shift` property must be set to <> 0 value before any encrypting or decrypting
        can be done.
        """
        self.shift = shift

    @uppercase_text
    def encrypt(self, text):
        if not self.shift:
            raise Exception('shift property is not set or 0')
        return self.shift_text(text, self.shift)

    @uppercase_text
    def decrypt(self, text):
        if not self.shift:
            raise Exception('shift property is not set or 0')
        return self.shift_text(text, self.shift * -1)

