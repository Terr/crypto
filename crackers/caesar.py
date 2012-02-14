from base import SubstitutionCipherCracker

from ciphers import CaesarCipher

from crypto.exceptions import CrackerException


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

        best_language = None
        best_result = ''
        best_score = 0

        for language in self.languages:
            # Count letter frequency
            frequencies = self.count_letter_frequency(self.text)
            encrypted_common_letter = self.most_common_letter(frequencies)

            # Calculate shift for the most common encrypted letter and letter in
            # the current language
            shift = self.get_letter_shift(encrypted_common_letter,
                                          language.get_common_letters()[0].upper())

            self.cipher.shift = shift
            result = self.cipher.decrypt(self.text)

            # See if words in the decrypted text match any of the most common
            # words of the language and keep track of the score
            common_words = [word.upper() for word in language.get_common_words()]
            score = 0

            for word in result.split():
                if word in common_words:
                    score += 1

            if score > 0:
                if score == best_score:
                    raise CrackerException(
                        'Cannot determine language as two languages got the same word ' \
                        'score (%(score)d): %(lang1)s and %(lang2)s. Try adding more most common words ' \
                        'to both languages' % {
                            'score': score,
                            'lang1': best_language,
                            'lang2': language
                    })
                elif score > best_score:
                    best_score = score
                    best_language = language
                    best_result = result

        if best_score == 0:
            raise CrackerException(
                'Could not judge decryption results as none of ' \
                'the registered languages returned a ' \
                'word score. Try adding more languages or more most ' \
                'common words.'
            )

        # Return our best guess as to the result
        return best_result
