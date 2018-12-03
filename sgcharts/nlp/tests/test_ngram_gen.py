# coding=utf-8
import unittest
import logging
from sgcharts.nlp import ngram_gen, ngram_from_tokens_gen

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)


class TestNgramGenerator(unittest.TestCase):

    def test_bigram(self):
        inp = "Apple is looking at buying U.K. startup for $1 billion"
        e = [('Apple', 'is'), ('is', 'looking'), ('looking', 'at'), ('at', 'buying'), ('buying', 'U.K.'),
             ('U.K.', 'startup'), ('startup', 'for'), ('for', '$1'), ('$1', 'billion')]
        a = list(ngram_from_tokens_gen(inp.split(), n=2))
        log.debug('a={}'.format(repr(a)))
        self.assertListEqual(a, e)

    def test_trigram(self):
        inp = "Apple is looking at buying U.K. startup for $1 billion"
        e = [('Apple', 'is', 'looking'), ('is', 'looking', 'at'), ('looking', 'at', 'buying'),
             ('at', 'buying', 'U.K.'), ('buying', 'U.K.', 'startup'), ('U.K.', 'startup', 'for'),
             ('startup', 'for', '$1'), ('for', '$1', 'billion')]
        a = list(ngram_gen(inp, n=3))
        self.assertListEqual(a, e)

    def test_fourgram(self):
        inp = "Apple is looking at buying U.K. startup for $1 billion"
        e = [('Apple', 'is', 'looking', 'at'),
             ('is', 'looking', 'at', 'buying'),
             ('looking', 'at', 'buying', 'U.K.'),
             ('at', 'buying', 'U.K.', 'startup'),
             ('buying', 'U.K.', 'startup', 'for'),
             ('U.K.', 'startup', 'for', '$1'),
             ('startup', 'for', '$1', 'billion')]
        a = list(ngram_gen(inp, n=4))
        self.assertListEqual(a, e)

    def test_fivegram(self):
        inp = "Apple is looking at buying U.K. startup for $1 billion"
        e = [('Apple', 'is', 'looking', 'at', 'buying'),
             ('is', 'looking', 'at', 'buying', 'U.K.'),
             ('looking', 'at', 'buying', 'U.K.', 'startup'),
             ('at', 'buying', 'U.K.', 'startup', 'for'),
             ('buying', 'U.K.', 'startup', 'for', '$1'),
             ('U.K.', 'startup', 'for', '$1', 'billion')]
        a = list(ngram_gen(inp, n=5))
        self.assertListEqual(a, e)

    def test_ngram_gen(self):
        inp = "Apple is looking at buying U.K. startup for $1 billion"
        e = [('Apple', 'is'), ('is', 'looking'), ('looking', 'at'), ('at', 'buying'), ('buying', 'U.K.'),
             ('U.K.', 'startup'), ('startup', 'for'), ('for', '$1'), ('$1', 'billion')]
        a = list(ngram_gen(inp, n=2))
        self.assertListEqual(a, e)
