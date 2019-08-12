import unittest
from collections import Counter
from occurence import occurence_count,open_file,close_file

class Tests(unittest.TestCase):
    def test_file_path(self):
        flag , file = open_file('dsadsadsadsadsa')
        self.assertFalse(flag)

    def test_word_count(self):
        self.assertEqual(
        occurence_count('Tejas Tejas is a Boy,? boY.'),
        Counter({'tejas': 2, 'boy': 2, 'is': 1, 'a': 1})
        )

    def test_close_file(self):
        file = open('wiki-en-train.word')
        flag = close_file(file)
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()
