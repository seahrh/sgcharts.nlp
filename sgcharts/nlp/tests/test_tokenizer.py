# coding=utf-8
import unittest
from sgcharts.nlp import tok


class TestTokenizer(unittest.TestCase):

    def test_dotted_acroynm_dollar_sign(self):
        text = "Apple is looking at buying U.K. startup for $1 billion"
        e = "Apple is looking at buying U.K. startup for $ 1 billion".split()
        a = tok(text)
        self.assertListEqual(a, e)

    def test_trailing_punctuation(self):
        text = "Who is he? Hello there! This is a sentence. How about this?!"
        e = "Who is he ? Hello there ! This is a sentence . How about this ? !".split()
        a = tok(text)
        self.assertListEqual(a, e)

    def test_infix_hyphen(self):
        text = "The 8 and 10-county definitions are not used for the greater Southern California Megaregion."
        e = ['The', '8', 'and', '10-county', 'definitions', 'are', 'not', 'used', 'for', 'the', 'greater',
             'Southern', 'California', 'Megaregion', '.']
        a = tok(text)
        self.assertListEqual(a, e)

    def test_contractions_pronoun(self):
        text = "i'll you'll've he'd shed it's we've they're"
        e = "i 'll you 'll've he 'd shed it 's we 've they 're".split()
        a = tok(text)
        print(a)
        self.assertListEqual(a, e)

    def test_contractions_verb(self):
        text = "can't couldn't don't doesn't didn't hadn't needn't shouldn't won't wouldn't"
        e = "ca n't could n't do n't does n't did n't had n't need n't should n't wo n't would n't".split()
        a = tok(text)
        print(a)
        self.assertListEqual(a, e)

    def test_apostrophe_s_infix_period(self):
        text = "Alibaba Group Holding Ltd. is setting up a $2 billion joint venture with billionaire Alisher " \
               "Usmanov's internet services firm Mail.ru Group Ltd. to strengthen the Chinese company's foothold in " \
               "Russian e-commerce. "
        text = text.lower()
        e = "alibaba group holding ltd . is setting up a $ 2 billion joint venture with billionaire alisher usmanov " \
            "'s internet services firm mail.ru group ltd . to strengthen the chinese company 's foothold in russian " \
            "e - commerce .".split()
        a = tok(text)
        self.assertListEqual(a, e)
