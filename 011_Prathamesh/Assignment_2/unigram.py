
# coding: utf-8

# ## Imports : regex, pandas, Counter from collections

# In[63]:


import re
import pandas
from collections import Counter


# #### Function to open a file in specified mode 

# In[30]:


def open_file(path,mode):
    try :
        file = open(path,mode)
        return True,file
    except Exception :
        return False, path


# #### Function to read file and return success, file 

# In[31]:


def read_file(file):
    try: 
        text = file.readlines()
        return True,text
    except Exception:
        return False, file


# #### Function to close file and return success status

# In[32]:


def close_file(file):
    try:
        file.close()
        return True
    except Exception:
        return False


# #### Function to count words in the file and return counter object or failure

# In[41]:


def count_words(train_text):
    try:
        word_counter = Counter()
        for line in train_text:
            word_counter.update(word for word in str('<s> '+re.sub(pattern=r'[!@#$%^&*()_\-\=\+.\/\\,<>?\'\"]+',repl="",string=line.lower().strip('\n'))+'</s>').split())
        return word_counter
    except Exception:
        return False


# #### Function to calculate probabilities of the word (unigram)

# In[56]:


def calculate_probabilities(word_counter):
    probablities={}
    total_words = sum(word_counter.values())
    probablities.update({word:(word_counter[word]/total_words)for word in word_counter.keys()})
    return probablities,total_words


# #### Function to store model i.e probabilities into a model file

# In[48]:


def save_model(probablities,path,name):
    Frame = pandas.DataFrame({'words':list(probablities.keys()),'probabilities':list(probablities.values())}).to_csv(path+name)
    return path+name


# #### Function to read model file and returns pandas.DataFrame type object

# In[52]:


def read_model(path):
    df = pandas.read_csv(path)
    df = df.drop(columns=df.columns[0],axis=1)
    return df


# #### Function to test model on test data with specified lambda value and returns entropy and coverage

# In[59]:


def test_model(text,model,total_words,lambda_known):
    lambda_1 = lambda_known
    lambda_uk = 1-lambda_1
    W = 0
    H = 0
    unk = 0
    for line in text:
        for word in str('<s> '+re.sub(pattern=r'[!@#$%^&*()_\-\=\+.\/\\,<>?\'\"]+',repl="",string=line.lower().strip('\n'))+'</s>').split():
            W+=1
            P = lambda_uk/total_words
            if word in list(model['words']):
                P += lambda_1*model[model.words==word]['probabilities'] 
            else:
                unk += 1
                H+=-numpy.log2(P)
    return H/W,(W-unk)/W


# In[60]:


flag_open_train,file_train = open_file('./wiki-en-train.word','r')
flag_read_train,train_text = read_file(file_train)
flag_close_train = close_file(file_train)
word_counter = count_words(train_text)
probabilities,vocab_size = calculate_probabilities(word_counter)
model_file = save_model(probabilities,'./','model_file.csv')
model = read_model(model_file)
flag_open_test,file_test = open_file('./wiki-en-test.word')
flag_read_test,test_text = read_file(file_test)
flag_close_test = close_file(file_test)
entropy,coverage = test_model(test_text,model,vocab_size,lambda_known=0.95)


# In[61]:


entropy


# In[62]:


coverage

