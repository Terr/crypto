import os
import difflib

from pprint import pprint
from unittest import TestCase

from ciphers import *
from crackers import *


def load_text(filename):
    return open(os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        'fixtures',
        filename
    ), 'r').read()

def diff(a, b):
    d = difflib.Differ()
    result = d.compare(a, b)
    # Only show differences
    filtered = list([x for x in result if x.startswith('+') or x.startswith('-') ])

    output = 'Assertion failed. Differences:\n'
    for i in xrange(0, len(filtered) - 1, 2):
        output += '%s\n%s\n\n' % (filtered[i], filtered[i+1])
    return output

class CaesarCipherTest(TestCase):
    def test_english(self):
        plain = load_text('english_plain.txt')
        expected = load_text('english_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3)
        self.assertEqual(cipher.shift, 3)

        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))

    def test_dutch(self):
        plain = load_text('dutch_plain.txt')
        expected = load_text('dutch_encrypted.txt')

        # Test with a shift of 3
        cipher = CaesarCipher(shift=3)
        encrypted = cipher.encrypt(plain)
        self.assertEqual(encrypted, expected, diff(encrypted, expected))
