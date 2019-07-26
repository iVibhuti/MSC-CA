from collections import Counter
import re

# opening the file and storing into string.
def openfile(filename):
    strh = ''
    try:
        fh = open(filename, encoding="utf8")
        strh = fh.read()
        return True, strh
    except Exception:
        return False,strh

# finding words and converting into lower case    
def getwordbins(words):
    return Counter(re.findall('[a-z]+', words.lower()))

# taking file name as input and using getwordbins method counting the words
def occurance(filename):
    status, file = openfile(filename)
    print(getwordbins(file))
    
# calling occurance method
occurance("./wiki-en-train.word")