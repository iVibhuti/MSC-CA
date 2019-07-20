import unittest
from collections import Counter
from word_occurance import openfile,word

class Test(unittest.TestCase):
    def test_file_path(self):
        flag , file = openfile('dsadsadsadsadsa')
        self.assertFalse(flag)
    
    def test_wrong_file_path(self):
        response, data = openfile('./wiki.word')
        self.assertFalse(response)
        
    def test_correct_word_count_1(self):
        response = word('I am abhinav.I am a boy.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'abhinav': 1,'a':1,'boy':1}))


    def test_correct_word_count_2(self):
        response = word('I AM abhinav.i am a StudenT.')
        self.assertEqual(response, Counter({'i': 2, 'am': 2, 'abhinav': 1,'a':1,'student':1}))

   
    def test_multiple_spaces_not_detected_as_a_word(self):
        response = word(' multiple   whitespaces')
        self.assertEqual(response, Counter({'multiple': 1, 'whitespaces': 1}))

    def test_expanded_list(self):
        response = word('one,\ntwo,\nthree')
        self.assertEqual(response, Counter({'one': 1, 'two': 1, 'three': 1}))

    
    def test_ignores_punctuation(self):
        response = word('car : carpet as python : pythonscript!!&@$%^&')
        self.assertEqual(response, Counter({'car': 1, 'carpet': 1, 'as': 1, 'python': 1, 'pythonscript': 1}))
    
            

if __name__ == '__main__':
    unittest.main()
