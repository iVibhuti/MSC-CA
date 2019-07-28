
# coding: utf-8
# Occurene of the words in the file
from collections import Counter
import re

#function to open the file and return file and boolean for presence of file in the input path.
def open_file(path):
    try :
        file = open(path,'r')
        return True,file
    except Exception :
        return False, path

#function to count occurance of each word in the file.
def count_occurence(text): 
    count = Counter()
    #to omit all the unnecessary punctuaions and symbols in the word.
    count.update(re.sub(r'[!@#$%^&*()_+={}|\\:"<>?;\',.\/ -]+','',word).lower() for word in text.split())
    #returns Counter type object.    
    return count

#function to close the opened file and return if it succeeds or not.
def close_file(file):
    try:
        file.close()
        return True
    except Exception:
        return False

#open file and read if the file exists.
flag, File = open_file('./wiki-en-train.word')
if flag:
    print(count_occurence(File.read()))
    close_file(File)
else :
    print('Error while reading file')

