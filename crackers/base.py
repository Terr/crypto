import string

from operator import itemgetter


class Cracker(object):
    pass


class SubstitutionCipherCracker(Cracker):
    def get_letter_shift(self, replaced_letter, expected_letter):
        """Returns the letter shift (number of alphabetical letters) between
        the encrypted `replaced_letter` and the decrypted `expected_letter`.

        Returns signed integer. Positive if the shift is 'to the right' (for
        ex. E is replaced with F).
        """
        rep_chr = ord(replaced_letter)
        exp_chr = ord(expected_letter)

        return (exp_chr - rep_chr) * -1

    def count_letter_frequency(self, text):
        """Counts alphabetical letters and returns dictionary containing
        letters as keys.
        """
        result = dict(zip(
            [x for x in string.letters], [0 for x in xrange(len(string.letters))]
        ))
        for l in text:
            if not l in string.letters:
                continue

            result[l] = result[l] + 1

        return result

    def most_common_letter(self, dict_frequencies):
        """Returns the letter with the most occurences in `dict_frequencies`.

        `dict_frequencies` should be a dictionary keyed with letters and a
        count as value.
        """
        if not len(dict_frequencies):
            raise Exception('Empty dictionary passed')

        sort = sorted(dict_frequencies.iteritems(), key=itemgetter(1))
        sort.reverse()
        return sort[0][0]

