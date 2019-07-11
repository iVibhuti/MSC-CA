from unittest import TestCase
from .word_count import WordCount


class Test_word_count(TestCase):

    def setUp(self):
        self.wc = WordCount()

    def test_word_count(self):
        self.assertEqual(0, len(self.wc.word_count("")))
        self.assertEqual({}, self.wc.word_count(""))
        self.assertEqual({}, self.wc.word_count("?!@#$%^&*({}|?><+=- "))
        self.assertEqual({'this':1, 'is':1, 'a':1, 'test':1}, self.wc.word_count("This is a test."))
        self.assertEqual(5, len(self.wc.word_count("This is a test.\n This is a another test.")))

    def test_word_report(self):
        pass

    def test_generate_report(self):
        pass

    def tearDown(self):
        del self.wc