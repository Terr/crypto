import os
import difflib
import chardet

from pprint import pprint
from unittest import TestCase

from ciphers import *
from crackers import *


def load_text(filename):
    """Loads fixture and returns contents in Unicode."""
    f = open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixtures',
        filename
    ), 'r')
    contents = f.read()
    encoding = f.encoding or chardet.detect(contents)['encoding']
    return contents.decode(encoding)

def diff(a, b):
    d = difflib.Differ()
    result = d.compare(a, b)
    # Only show differences
    filtered = list([x for x in result if x.startswith('+') or x.startswith('-') ])

    num_diffs_shown = min(6, len(filtered) - 1)
    output = 'Assertion failed. Differences (showing %d):\n' % (num_diffs_shown / 2)
    for i in xrange(0, num_diffs_shown, 2):
        output += '%s\n%s\n\n' % (filtered[i], filtered[i+1])
    return output

class CaesarCipherTest(TestCase):
    def test_all_uppercase(self):
        plain = load_text('english_plain.txt')
        expected = load_text('english_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3)
        self.assertEqual(cipher.shift, 3)

        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))

    def test_source_not_uppercase(self):
        plain = load_text('dutch_plain.txt')
        expected = load_text('dutch_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3)
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

    def test_esperanto(self):
        """Esperanto has a higher 'A' frequency instead of 'E', like most
        Western languages.
        """
        plain = load_text('esperanto_plain.txt').upper() # Source is in mixed case
        encrypted = load_text('esperanto_encrypted.txt')

        cracker = CaesarCracker(encrypted)
        result = cracker.run()
        self.assertEqual(result, plain, diff(result, plain))

