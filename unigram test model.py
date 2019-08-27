#!/usr/bin/env python
# coding: utf-8

# In[9]:


import io
import math
import argparse
from collections import defaultdict


# In[10]:


EOS = '<s>'
lambda_1 = 0.95
lambda_unk = 1 - lambda_1
v = 1e6 #vocabulary size


# In[11]:


def load_model(model_file):
    probabilities = defaultdict(float)
    with open(model_file,'r') as f:
        for line in f:
            word,probability = line.strip().split('\t')
            probabilities[word] = float(probability)
        return probabilities


# In[12]:


def test_unigram(probabilities,test_file):
    w = 0 #total no of words
    unk = 0 #number of unknown words
    h = 0 #negative log likelihood
    
    with open(test_file,'r') as f:
        for line in f:
            words = line.strip().split(' ')
            words.append(EOS)
            for word in words:
                w += 1
                p = lambda_unk / v
                if word in probabilities:
                    p += lambda_1 * probabilities[word]
                else:
                    unk += 1
                h += - math.log2(p)
                
        
    #entropy h is average negative log2 likelihood per word
    print('Entropy: {}'.format(h/w))
    #coverage is the percentage of known words in the corpus
    print('Coverage: {}'.format((w - unk)/w))
             
    


# In[42]:


load_model("../text analysis/model1.txt")


# In[46]:


test_unigram("4","../Documents/wiki-en-test.word")


# In[ ]:




