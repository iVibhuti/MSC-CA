#!/usr/bin/env python
# coding: utf-8

# In[68]:


import io
import argparse


# In[69]:


EOS = '</s>'


# In[94]:


def train_unigram(training_file,model_file):
    counts = {}
    total_count = 0
    with open(training_file,'r' ) as f:
        for line in f:
            words = line.strip().split(' ')
            words.append(EOS)
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
                total_count += 1
    probabilities = {}
    for word,count in counts.items():
        probabilities[word] = count / total_count
        
    #write the info in buffer
    out = io.StringIO()
    for word,probability in sorted(probabilities.items(),key = lambda x: x[1],reverse = True):
        out.write('{}\t{}\n'.format(word,probability))
        
    if model_file == 'stdout':
        print(out.getvalue().strip())
    else:
        with open(model_file,'w') as f:
            f.write(out.getvalue().strip())

    


# In[95]:


train_unigram("../Documents/wiki-en-train.txt","../text analysis/model1.txt")


# In[ ]:





# In[ ]:




