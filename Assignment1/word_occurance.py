#--------------------------------------------------------------#
# Author : Abhinav Anil
# PRN : 18030142001
# Programme : M.Sc. CA
# Course : Text Analytics

# Problem Statment : Find the Frequency of each word from the given text.
#--------------------------------------------------------------#

#-----------------Import necessary packages--------------------#


from collections import Counter 				
import re 							

#--------------------------------------------------------------#

#-----------------------Functions------------------------------#

#Using function openfile to read file with the exception handling
def openfile(filename):						
    string = ''							
    try:							
        files = open(filename, encoding="utf8")			
        string = files.read()					
        return True, string					
    except Exception:						
        return False,string

# Closing the file
def close_file(filename):
    try:
        files.close()
        return True
    except Exception:
        return False
    
#create fundton word and convert each word from file in lower case
        
def word(words):						
    return Counter(re.findall('[a-z]+', words.lower()))		
#create function occurence to print the word from file by passing the file name in it.
def occurance(filename):					
    status, file = openfile(filename)				
    print(word(file))					

occurance("wiki-en-train.word")					
