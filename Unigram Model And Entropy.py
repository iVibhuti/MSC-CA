#!/usr/bin/env python
# coding: utf-8

# In[3]:


from nltk.tag import UnigramTagger 
from nltk.corpus import treebank 
import numpy as np
import pandas as pd
#from docx import Document


# # Reading the wiki-en-train file

# In[42]:


import docx2txt
train = docx2txt.process("/Users/shashankshivam/Desktop/wiki-en-train.docx")
print(train)


# In[43]:


import nltk
from nltk import word_tokenize
from nltk.util import ngrams
from collections import Counter
nltk.download('punkt')


# # Creating the token

# In[44]:


token = nltk.word_tokenize(train)


# In[45]:


token


# # Creating unigram model

# In[59]:


unigram = ngrams(token,1)
bigrams = ngrams(token,2)
trigrams = ngrams(token,3)
fourgrams = ngrams(token,4)
fivegrams = ngrams(token,5)


# In[60]:


Counter(unigram)


# In[48]:


Counter(trigrams)


# # Reading the wiki-en-text file

# In[50]:


test = docx2txt.process("/Users/shashankshivam/Desktop/wiki-en-test.docx")
print(test)


# # Calculating the entropy of test file

# In[55]:


import math, string, sys, fileinput
def entropy(data, iterator=range_bytes):
    if not data:
        return 0
    entropy = 0
    for x in iterator():
        p_x = float(data.count(chr(x)))/len(data)
        if p_x > 0:
            entropy += - p_x*math.log(p_x, 2)
    return entropy


# In[62]:


entropy(test)


# In[ ]:




