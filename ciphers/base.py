import re
import string

from operator import itemgetter

from crypto_exceptions import CipherException


class Cipher(object):
    """Abstract class"""

    def __init__(self, *args, **kwargs):
        super(Cipher, self).__init__()

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()


class SubstitutionCipher(Cipher):
    """Simple substitution cipher that only works with uppercase alphabetical
    letters.
    """

    def __init__(self, shift, character_list=string.uppercase,
                 preserve_chars='', *args, **kwargs):
        """Initialize substitution cipher with a `shift`.

        :param shift: Number of characters to shift when encrypting and
        decrypting. Must be set to <> 0 value.
        :param character_list: Strign or list of individual characters that
        form up the cipher alphabet. The order of the list is important.
        """
        super(SubstitutionCipher, self).__init__(*args, **kwargs)

        self.shift = shift
        self.character_list = character_list
        self.character_list_len = len(self.character_list)
        self.preserve_chars = preserve_chars

    def encrypt(self):
        raise NotImplementedError()

    def decrypt(self):
        raise NotImplementedError()

    def shift_character(self, char, shift):
        """Shifts *alphabetical* characters `shift` number
        of characters to the 'right' (or 'left' if `shift` is negative).

        Returns text in encrypted form, in uppercase.
        """
        if char in self.preserve_chars:
            # Preserve character
            return char
        elif char not in self.character_list:
            # Remove characters that are not in the charset
            return ''

        # TODO If performance becomes an issue, convert character list search
        # to binary search
        new_char_pos = self.character_list.index(char) + shift

        if new_char_pos >= self.character_list_len:
            new_char_pos = new_char_pos - self.character_list_len
        elif new_char_pos < 0:
            new_char_pos = self.character_list_len + new_char_pos

        return self.character_list[new_char_pos]

    def shift_text(self, text, shift):
        """Shifts value in :attr:`text` with `shift` characters."""
        mutated_text = ''

        for s in text:
            mutated_text += self.shift_character(s, shift)

        return mutated_text

    def remove_spacing(self, text):
        """Remove spacing (whitespaces, newlines) from `text`."""
        return re.sub('\s', '', text)
