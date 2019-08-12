import unittest
from collections import Counter
from word_occurance import openfile,getwordbins

class Test(unittest.TestCase):
    def test_wrong_file_path(self):
        response, data = openfile('./wiki.word')
        self.assertFalse(response)
    def test_correct_word_count_1(self):
        response = getwordbins('I am sarthak.I am a boy.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'sarthak': 1,'a':1,'boy':1}))
    def test_correct_word_count_2(self):
        response = getwordbins('I AM SARTHAK.i am a StudenT.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'sarthak': 1,'a':1,'student':1}))
if __name__ == '__main__':
    unittest.main()
