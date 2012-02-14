import yaml
import os


class Language(object):
    """Loads language data from :attr:`self.language`.txt."""

    filename = None
    english_language_name = None
    native_language_name = None

    common_letters = None
    """Ordered list or string of the most common letters in the language."""
    common_words = None
    """Ordered list of most common words in the language."""

    def __init__(self):
        if not self.filename:
            raise ValueError('Class %s\'s filename property has no value' %
                             self.__class__.__name__)

        try:
            lang_file = open('%s' % os.path.join(
                os.path.dirname(__file__),
                'data',
                '%s.yaml' % self.filename
            ), 'r')
        except IOError, e:
            raise
        else:
            # Read data
            lang_contents = lang_file.read()

            # Parse data
            lang_data = yaml.load(lang_contents)

            # Set data
            for key, value in lang_data.iteritems():
                setattr(self, key, value)

            lang_file.close()

    def __getattr__(self, name):
        if name.startswith('get_'):
            name = name[4:]
            result = getattr(self, name)
            if not result:
                raise ValueError('%s property is empty' % name)
            return lambda: result
        raise AttributeError

    #def get_common_letters(self):
    #    if not self.common_letters:
    #        raise ValueError('common_letters property is empty')
    #    return self.common_letters

    def __unicode__(self):
        return u'%s (%s)' % (self.english_language_name, native_language_name)
