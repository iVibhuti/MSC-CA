import numpy
import re
import pandas
from collections import Counter


# Open a file  
def open_file(path,mode):
    try :
        file = open(path,mode)
        return True,file
    except Exception :
        return False, path


# Read file and return 
def read_file(file):
    try: 
        text = file.readlines()
        return True,text
    except Exception:
        return False, file


# To close file and return status
def close_file(file):
    try:
        file.close()
        return True
    except Exception:
        return False


# To count words in the file and return counter object or failure
def count_words(trn_text):
    try:
        word_counter = Counter()
        for line in trn_text:
            word_counter.update(word for word in str('<s> '+re.sub(pattern=r'[!@#$%^&*()_\-\=\+.\/\\,<>?\'\"]+',repl="",string=line.lower().strip('\n'))+'</s>').split())
        return word_counter
    except Exception:
        return False


# To calculate probabilities of the word (unigram)
def calculate_probabilities(word_counter):
    probablities={}
    total_words = sum(word_counter.values())
    probablities.update({word:(word_counter[word]/total_words)for word in word_counter.keys()})
    return probablities,total_words


# To store model i.e probabilities into a model file
def save_model(probablities,path,name):
    Frame = pandas.DataFrame({'words':list(probablities.keys()),'probabilities':list(probablities.values())}).to_csv(path+name)
    return path+name


# To read model file and returns pandas.DataFrame type object
def read_model(path):
    df = pandas.read_csv(path)
    df = df.drop(columns=df.columns[0],axis=1)
    return df


# To test model on test data with specified lambda value and returns entropy and coverage
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




flg_open_trn,file_trn = open_file('./wiki-en-trn.word','r')
flg_read_trn,trn_text = read_file(file_trn)
flg_close_trn = close_file(file_trn)
word_counter = count_words(trn_text)
probabilities,vocab_size = calculate_probabilities(word_counter)
model_file = save_model(probabilities,'./','model_file.csv')
model = read_model(model_file)
flg_open_test,file_test = open_file('./wiki-en-test.word','r')
flg_read_test,test_text = read_file(file_test)
flg_close_test = close_file(file_test)
entropy,coverage = test_model(test_text,model,vocab_size,lambda_known=0.95)

entropy

coverage
