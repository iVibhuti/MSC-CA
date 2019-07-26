import unittest
from collections import Counter
from word_occurance import openfile,getwordbins

# defining class with required methods
class Test(unittest.TestCase):
    # testing file path
    def test_wrong_file_path(self):
        response, data = openfile('./wiki.word')
        self.assertFalse(response)
    # testing getwordsbin method    
    def test_correct_word_count_1(self):
        response = getwordbins('I am Subodh.I am a boy.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'subodh': 1,'a':1,'boy':1}))
    # checking with camelcase
    def test_correct_word_count_2(self):
        response = getwordbins('I AM SUBODH.i am a StudenT.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'subodh': 1,'a':1,'student':1}))
if __name__ == '__main__':
    unittest.main()
