#!/usr/bin/env python
# coding: utf-8

# In[3]:


import unittest
from collections import Counter

class Tests(unittest.TestCase):
    def test_file_path(self):
        flag , file = open_file('dsadsad')
        self.assertFalse(flag)

    def test_count_one_word(self):
        self.assertEqual(
            occurence_count('word'),
            {'word': 1}
        )

    def test_word_count(self):
        self.assertEqual(
        occurence_count('We will will play cricket cricket.'),
        Counter({'we': q, 'will': 2, 'play': 1, 'cricket': 2})
        )
        
    def test_count_one_of_each(self):
        self.assertEqual(
            occurence_count('one of each'),
            {'one': 1, 'of': 1, 'each': 1}
        )
    def test_cramped_list(self):
        self.assertEqual(
            occurence_count('one,two,three'),
            {'one': 1, 'two': 1, 'three': 1}
        )
    def test_expanded_list(self):
        self.assertEqual(
            occurence_count('one,\ntwo,\nthree'),
            {'one': 1, 'two': 1, 'three': 1}
        )
        def test_ignores_punctuation(self):
            self.assertEqual(
                occurence_count('car : carpet as python : pythonscript!!&@$%^&'),
                {'car': 1, 'carpet': 1, 'as': 1, 'python': 1, 'pythonscript': 1}
        )

    def test_include_numbers(self):
        self.assertEqual(
            occurence_count('testing 1 2 testing'),
            {'testing': 2, '1': 1, '2': 1}
        )

    def test_normalize_case(self):
        self.assertEqual(
            occurence_count('go Go GO Stop stop'),
            {'go': 3, 'stop': 2}
        )

    def test_apostrophes(self):
        self.assertEqual(
            occurence_count("First: don't laugh. Then: don't cry."),
            {'first': 1, "don't": 2, 'laugh': 1, 'then': 1, 'cry': 1}
        )

    def test_quotations(self):
        self.assertEqual(
            occurence_count("Joe can't tell between 'large' and large."),
            {'joe': 1, "can't": 1, 'tell': 1, 'between': 1, 'large': 2,
             'and': 1}
        )

    def test_multiple_spaces_not_detected_as_a_word(self):
        self.assertEqual(
            occurence_count(' multiple   whitespaces'),
            {'multiple': 1, 'whitespaces': 1}
        )


    def test_close_file(self):
        file = open('./wiki-en-train')
        flag = close_file(file)
        self.assertTrue(flag)

if __name__ == '__main__':
    unittest.main()


# In[ ]:




