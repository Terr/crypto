#!/usr/bin/python
import os
import sys
import importlib

sys.path.insert(
    0, os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        os.pardir
    )
)
import argparse

import ciphers


# Build list of cipher classes
def get_subclasses(cls):
    """Iterators through subclasses for baseclass `cls` and returns a list of
    classes that have no subclasses of their own.
    """
    klasses = []
    for klass in cls.__subclasses__():
        if not klass.__subclasses__():
            return klass
        else:
            klass_to_append = get_subclasses(klass)
            if klass_to_append:
                klasses.append(klass_to_append)

    return klasses

parser = argparse.ArgumentParser(description='Encrypt file with chosen cipher.')

parser.add_argument(
    'input_filename',
    type=str,
    help='File to encrypt',
)
parser.add_argument(
    'output_filename',
    type=str,
    help='Destination file',
)
parser.add_argument(
    '-c', '--cipher',
    type=str,
    help='Cipher to use (%s)' % ', '.join([x.__name__ for x in get_subclasses(ciphers.Cipher) ]),
    default='CaesarCipher'
)
parser.add_argument(
    '-s', '--shift',
    type=int,
    help='Character shift to use (used for substitution ciphers)',
)


args = parser.parse_args()

if os.path.exists(args.output_filename):
    print 'Output file already exists. Aborting.'
    sys.exit()

if not os.path.exists(args.input_filename):
    print 'Input file doesn\'t exist. Aborting.'
    sys.exit()


plain_file = open(args.input_filename, 'r')
plain_text = plain_file.read()
plain_file.close()

cipher_klass = getattr(ciphers, args.cipher)
cipher = cipher_klass(**dict(args._get_kwargs()))
result = cipher.encrypt(plain_text)

encrypted_file = open(args.output_filename, 'w')
encrypted_file.write(result)
encrypted_file.close()

print 'Done encrypting contents of "%s" and writing to "%s"' % (
    args.input_filename,
    args.output_filename,
)
