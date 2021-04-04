from django.test import TestCase
from core.models import *


class TestLanguage(TestCase):

    def test_str_format(self):
        """Test the appearance of Languages as used in the make_paste template."""
        self.assertEqual(str(Language.objects.create(name='thing 1')),
                         'thing 1')

    SORTED = [
        'a',
        'thing 1',
        'Thing 2',
        'thing 3',
        'THIS',
    ]

    def test_sort(self):
        """Test that there is a sort order for Language objects."""
        def create(name):
            return Language.objects.create(name=name)

        create('thing 3')
        create('THIS')
        create('thing 1')
        create('a')
        create('Thing 2')

        ordering = [lang.name for lang in Language.objects.all()]
        self.assertEqual(ordering, self.SORTED)


class TestPaste(TestCase):

    def test_hits(self):
        """Test when a paste is viewed, the hit counter increments."""
        p = Paste.objects.create(title='title', body='body')
        self.assertEqual(p.hits, 0)
        self.assertEqual(Paste.objects.get(pk=p.pk).hits, 0)
        p.view()
        self.assertEqual(p.hits, 1)
        self.assertEqual(Paste.objects.get(pk=p.pk).hits, 1)

    def test_frozen_hits(self):
        """Test the paste freeze_hits flag prevents further hits from being counted."""
        p = Paste.objects.create(title='title', body='body')
        p.hits = 123
        p.freeze_hits = True
        p.save()
        p.view()
        self.assertEqual(p.hits, 123)
        self.assertEqual(Paste.objects.get(pk=p.pk).hits, 123)

    def test_get_absolute_url(self):
        """Used to get a permalink in the templates."""
        p = Paste.objects.create(title='title', body='body')
        self.assertEqual(p.get_absolute_url(), f'/{p.pk}')
        p2 = Paste.objects.create(title='title2', body='body2')
        self.assertEqual(p2.get_absolute_url(), f'/{p2.pk}')

    def test_size(self):
        """Test size set based on title + body size"""
        T, B = 20, 15
        p = Paste.objects.create(title='t' * T, body='b' * B)
        self. assertEqual(p.size, T+B)

        T2, B2 = 10, 7
        p.title = 'T' * T2
        p.body = 'B' * B2
        p.save()
        self. assertEqual(p.size, T2+B2)
