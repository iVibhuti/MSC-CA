"""
NAME: Shubham Kumar
PRN: 18030142032
PROGRAM: MSc. C.A.(DS)
"""
import os
from unittest import TestCase
from .word_count import WordCount


class TestWordCount(TestCase):
    write_file = './report_test.txt'
    file = './test/wiki-en-train.word'

    def setUp(self):
        self.wc = WordCount()

    def test_word_count(self):
        self.assertEqual(len(self.wc.word_count("")), 0)
        self.assertEqual(self.wc.word_count(""), {})
        self.assertEqual(self.wc.word_count("?!@#$%^&*(){}|?><+=- /*:;.,~`"), {})
        self.assertEqual(self.wc.word_count("This is a test."), {'this': 1, 'is': 1, 'a': 1, 'test': 1})
        self.assertEqual(len(self.wc.word_count("This is a test.\n This is a another test.")), 5)

    def test_word_report(self):
        count = len(self.wc.word_report(filename=TestWordCount.file, special_chars='(LRB|RRB)'))
        self.assertTrue(count, 4476)

    def test_generate_report_unique(self):
        word_dict = self.wc.word_report(filename=TestWordCount.file, special_chars='(LRB|RRB)')
        self.wc.generate_report(filename=TestWordCount.write_file, word_count=word_dict, unique=True)
        content = None
        try:
            with open(TestWordCount.write_file, 'r', encoding="utf-8") as file:
                content = file.read()
        except Exception as e:
            print(e)
        os.remove(TestWordCount.write_file)
        # Testing generated file content.
        self.assertTrue(content, "Number of unique words:2143")


    def test_generate_report_total_word(self):
        word_dict = self.wc.word_report(filename=TestWordCount.file, special_chars='(LRB|RRB)')
        self.wc.generate_report(filename=TestWordCount.write_file, word_count=word_dict, unique=False)
        content = None
        try:
            with open(TestWordCount.write_file, 'r', encoding="utf-8") as file:
                content = file.read()
        except Exception as e:
            print(e)
        os.remove(TestWordCount.write_file)
        # Testing generated file content.
        self.assertTrue(content, "Total number of words:4476")

    def tearDown(self):
        del self.wc
