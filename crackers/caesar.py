from base import SubstitutionCipherCracker

from ciphers import CaesarCipher


class CaesarCracker(SubstitutionCipherCracker):
    """Provides functionality for cracking a CaesarCipher."""

    def __init__(self, text):
        self.text = text
        self.cipher = CaesarCipher(text)

    def run(self):
        """Attempts to figure out the letter shift to decrypt the text
        by counting the letter frequency and trying to find the corresponding
        encrypted version of `most_common_letter`, which depends on the language
        the text is in.
        """

        # Count letter frequency
        frequencies = self.count_letter_frequency(self.text)
        encrypted_common_letter = self.most_common_letter(frequencies)

        # Calculate shift for what we assume is the 'E'
        shift = self.get_letter_shift(encrypted_common_letter, 'E')

        self.cipher.shift = shift
        return self.cipher.decrypt(self.text)

