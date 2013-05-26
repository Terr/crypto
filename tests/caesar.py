import string
import os
import difflib
import chardet

from unittest import TestCase

from crypto.ciphers import *
from crypto.crackers import *


def load_text(filename):
    """Loads fixture and returns contents in Unicode."""
    f = open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixtures',
        filename
    ), 'r')
    contents = f.read().strip()
    encoding = f.encoding or chardet.detect(contents)['encoding']
    f.close()
    return contents.decode(encoding)

def diff(a, b):
    d = difflib.Differ()
    result = d.compare(a, b)
    # Only show differences
    filtered = list([x for x in result if x.startswith('+') or x.startswith('-')])

    num_diffs_shown = min(6, len(filtered) - 1)
    output = 'Assertion failed. Differences (showing %d):\n' % (num_diffs_shown
                                                                / 2)
    for i in xrange(0, num_diffs_shown, 2):
        output += '%s\n%s\n\n' % (filtered[i], filtered[i + 1])
    return output

class CaesarCipherTest(TestCase):
    def test_simple_encryption(self):
        """Simple test to determine if the caesar cipher works at all."""

        plain = load_text('english_simple_plain.txt')
        expected = load_text('english_simple_encrypted.txt')

        cipher = CaesarCipher(
            shift=3, character_list=string.uppercase
        )
        encrypted = cipher.encrypt(plain.upper())
        self.assertEqual(encrypted, expected, diff(encrypted, expected))

    def test_simple_decryption(self):
        """Simple test to determine if the caesar cipher works at all."""

        encrypted = load_text('english_simple_encrypted.txt')
        expected = load_text('english_simple_plain.txt')
        # Spaces have been removed during encryption, and converted to
        # uppercase
        expected = expected.replace(' ', '').upper()

        cipher = CaesarCipher(
            shift=3, character_list=string.uppercase
        )
        plain = cipher.decrypt(encrypted.upper())
        self.assertEqual(plain, expected, diff(plain, expected))

    def test_with_character_preservation(self):
        plain = load_text('english_plain.txt')
        expected = load_text('english_encrypted.txt')

        # Test with a shift of 3
        preserve_chars = string.digits + string.whitespace + string.punctuation
        cipher = CaesarCipher(shift=3, preserve_chars=preserve_chars)
        self.assertEqual(cipher.shift, 3)

        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))

    def test_mix_lower_and_uppercase(self):
        plain = load_text('dutch_plain.txt')
        expected = load_text('dutch_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3, character_list=string.uppercase +
                              string.lowercase)
        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))

    def test_special_characters(self):
        plain = load_text('esperanto_plain.txt')
        expected = load_text('esperanto_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3)
        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))


class CaesarCrackerTest(TestCase):
    """Test for Caesar cipher cracker."""

    def test_english(self):
        plain = load_text('english_plain.txt')
        encrypted = load_text('english_encrypted.txt')

        cracker = CaesarCracker(encrypted)
        result = cracker.run()
        self.assertEqual(result, plain, diff(result, plain))

    def test_dutch(self):
        plain = load_text('dutch_plain.txt').upper() # Source is in mixed case
        encrypted = load_text('dutch_encrypted.txt')

        cracker = CaesarCracker(encrypted)
        result = cracker.run()
        self.assertEqual(result, plain, diff(result, plain))

        # National anthem of The Netherlands
        plain = load_text('dutch_anthem_plain.txt').upper() # Source is in mixed case
        encrypted = load_text('dutch_anthem_encrypted.txt')

        cracker = CaesarCracker(encrypted)
        result = cracker.run()
        self.assertEqual(result, plain, diff(result, plain))

    def test_esperanto(self):
        """Esperanto has a higher 'A' frequency instead of 'E', like most
        Western languages.
        """
        plain = load_text('esperanto_plain.txt').upper() # Source is in mixed case
        encrypted = load_text('esperanto_encrypted.txt')

        cracker = CaesarCracker(encrypted)
        result = cracker.run()
        self.assertEqual(result, plain, diff(result, plain))

