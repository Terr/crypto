"""Western languages."""
# -*- coding: utf-8 -*-

from base import Language


class EnglishLanguage(Language):
    filename = 'english'
    english_language_name = 'English'
    native_language_name = 'English'


class DutchLanguage(Language):
    filename = 'dutch'
    english_language_name = 'Dutch'
    native_language_name = 'Nederlands'


class EsperantoLanguage(Language):
    filename = 'esperanto'
    english_language_name = 'Esperanto'
    native_language_name = 'Esperanto'
