#!/usr/bin/env python
# coding: utf-8

# In[18]:


from collections import defaultdict
import re


# In[19]:


def word_occurence(para):
    freq = defaultdict(int)
    words = para.split(" ")
    for word in words:
        word = re.sub('[^A-Za-z]+', '', word)
        freq[word] += 1
    return dict(freq)


# In[20]:


# testing
para = open('para.word', 'r', encoding='utf8').read()
word_occurence(para)


# In[23]:


# test cases
import unittest
import os
import sys 
class Test_word_occurence(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.isfile('para.word'))
    
    def test_file_content_exists(self):
        self.assertTrue(os.stat('para.word').st_size != 0)
    
    def test_file_content_type(self):
        self.assertEqual(type(para), str)
        
    # to assert that the returned value is a dict 
    def test_return_value_type(self):
        self.assertEqual(type(word_occurence(para)), dict)
        
    def test_return_value_size(self):
        self.assertTrue(len(word_occurence(para)) != 0)
    
    
    
if __name__ == '__main__':
    unittest.main(argv='v', exit = False)

