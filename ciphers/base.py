import string

from operator import itemgetter


class Cipher(object):
    """Abstract class"""

    def __init__(self, shift=None, *args, **kwargs):
        super(Cipher, self).__init__()

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()


class SubstitutionCipher(Cipher):
    """Simple substitution cipher that only works with uppercase alphabetical
    letters.
    """
    ORD_A = ord('A')
    ORD_Z = ord('Z')

    def __init__(self, shift=None, *args, **kwargs):
        """Initialize cipher with optional `shift`.

        `shift` property must be set to <> 0 value before any encrypting or decrypting
        can be done.
        """
        super(SubstitutionCipher, self).__init__(*args, **kwargs)

        self.shift = shift

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def shift_character(self, char, shift):
        """Shifts *alphabetical* character `shift` number of characters to the
        'right' (or 'left' if `shift` is negative).
        """
        if char not in string.uppercase:
            return char

        new_ord = ord(char) + shift
        if new_ord > self.ORD_Z:
            new_ord = self.ORD_A + (new_ord - self.ORD_Z) - 1
        elif new_ord < self.ORD_A:
            new_ord = self.ORD_Z - (self.ORD_A - new_ord) + 1

        return chr(new_ord)

    def shift_text(self, text, shift):
        """Shifts value in :attr:`text` with `shift` characters."""
        mutated_text = ''

        for s in text:
            mutated_text += self.shift_character(s, shift)

        return mutated_text
