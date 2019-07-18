#--------------------------------------------------------------#
# Author : Aditya Pandit
# PRN : 18030142021
# Programme : M.Sc. CA
# Course : Text Analytics

# Problem Statment : Find the Frequency of each word from the given text/corpus
#--------------------------------------------------------------#

#-----------------Import necessary packages--------------------#

import re
from collections import Counter

#--------------------------------------------------------------#

#-----------------------Functions------------------------------#

# function : open_file_connection
# function objective : open a connection to a file
# inputs : file path
# returns : connection status, file object

def open_file_connection(path, *, file = ''):
	try:
		file = open(path, encoding = 'utf8')
		return True, file
	except Exception:
		return False, file


# function : word_count
# function objective : give word count of each word in the given text
# inputs : text
# returns : Counter object

def word_count(text):
	return Counter(re.findall('[a-z]+', text.lower()))


# function : close_file_connection
# function objective : close the connection to the file
# inputs : file object
# returns : connection status

def close_file_connection(file):
	try:
		file.close()
		return True
	except Exception:
		return False

#--------------------------------------------------------------#

#-----------------------Main Execution-------------------------#

if __name__ == '__main__':

	status, file = open_file_connection('./wiki-en-train.word')
	
	if status:
		print('-------------------------')
		print('File Name: ', file.name)
		print('-------------------------')
		print('Word Frequencies:')
		print(word_count(file.read()))
		close_file_connection(file)
	else:
		print("There was some error reading the file.")

#--------------------------------------------------------------#