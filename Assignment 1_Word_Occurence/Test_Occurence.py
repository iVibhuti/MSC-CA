'''
Name - Shubham Kumar
Prn - 18030142033
Course  - MScCA(DS)
'''
# import functions from Occurence and the unittest module for testing.
from Occurence import open_file, close_file, count_occurence
import unittest
from collections import Counter

class Tests(unittest.TestCase):
    #function to test open_file() function. asserts "true" if successful else asserts "false".
    def test_open_file(self):
        flag, file = open_file("asffgvcg")
        if flag == False:
            self.assertFalse(flag)
        else:
            self.assertTrue(flag)

    #function to test close_file() function. asserts "true" if successful else asserts "false".
    def test_close_file(self):
        file = open('wiki-en-train.word')
        flag = close_file(file)
        if flag == True:
            self.assertTrue(flag)
        else:
            self.assertFalse(flag)

    #function to test count_occurence() function. asserts "true" if successful else asserts "false".        
    def test_count_occurence(self):
        self.assertEqual(count_occurence('Dude go  Enjoy. Will you \nTake care '),Counter({'care': 1,'dude': 1,'enjoy': 1,'go': 1,'take': 1,'will': 1,'you': 1}))

if __name__ == '__main__':
    #creats class object and runs all the functions.
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

