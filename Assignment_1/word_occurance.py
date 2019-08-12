'''
Name : Sarthak Mahendra
Prn  : 18030142028
Class:	MSC-CA (Data Science)
Symbiosis Institute of Computer Studies and Research, Pune
'''
from collections import Counter 				# Imported Counter Class from Collection module
import re 							# Imported Regular Expression for matching patterns

def openfile(filename):						# Function decleration with arguments for open file
    strh = ''							# String variable decleration
    try:							# Exception raising block if file not found
        fh = open(filename, encoding="utf8")			# Function open a file if found and return file object 
        strh = fh.read()					# It's read the file object and returns the content in string
        return True, strh					# If file opened without exception then returns "True" and value of string variable
    except Exception:						# If exception raised in try block then this block will execute
        return False,strh					# It return "False" no value as type string
        
def getwordbins(words):						# Function decleration with arguments for word counting
    return Counter(re.findall('[a-z]+', words.lower()))		# Finding the characters in string and converting them into lowercase and return total no of count

def occurance(filename):					# Function decleration with arguments performing main operation, calling both function declared above
    status, file = openfile(filename)				# Function calling openfile and passing file name as arguments and it returns status and value present in file
    print(getwordbins(file))					# Print function prints the outcome received by calling getwordbins function by passing file object as arguments

occurance("wiki-en-train.word")					# Main Function calling and passing filename as arguments
