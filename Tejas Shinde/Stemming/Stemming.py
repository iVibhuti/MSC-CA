import re

def stem_string(string):
    if type(string) is not str:
        return ('Not a valid String.')
    stemmed = ''
    for word in string.split():
        stemmed = stemmed + ' ' + re.sub('ing$|ed$|er$' , '' , word)
    if stemmed.strip() != string :
        return ('Stemmed Sentence : ' + stemmed)
    else:
        return ('No Stemming done, as there are no words to be stemmed')

string = input('Enter a string : ')
print(stem_string(string))

# def occurence_count(text):
