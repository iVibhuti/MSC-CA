#----------------------------------------------------------------------------#
# Author : Aditya Pandit
# PRN : 18030142021
# Programme : M.Sc. CA
# Course : Text Analytics

# Problem Statment : Test the integrity of Frequency.py code
#----------------------------------------------------------------------------#

#-----------------------Import necessary packages----------------------------#

import unittest
from collections import Counter
from Frequency import open_file_connection
from Frequency import close_file_connection
from Frequency import word_count

#----------------------------------------------------------------------------#

#-------------------------------Test Cases-----------------------------------#

class Test(unittest.TestCase):

	# function to test the response when wrong file path is passed to the
	# function open_file_connection
	def test_wrong_file_path(self):
		response, data = open_file_connection('./wiki.word')
		self.assertFalse(response)

	# function to test the response when correct file path is passed to the
	# function open_file_connection
	def test_correct_file_path(self):
		response, data = open_file_connection('./wiki-en-train.word')
		self.assertTrue(response)
		data.close()

	# function to test the response when file is being closed using
	# function close_file_connection
	def test_file_close(self):
		file = open('./wiki-en-train.word')
		response = close_file_connection(file)
		self.assertTrue(response)

	# function to test whether the function word_count returns correct number
	# of frequencies
	def test_correct_word_count_1(self):
		response = word_count('I am Aditya. I am a boy.')
		self.assertEqual(response, Counter({'i': 2, 'am': 2, 'aditya': 1, 'a': 1, 'boy': 1}))
	
	# function to test whether the function word_count returns correct number
	# of frequencies
	def test_correct_word_count_2(self):
		response = word_count('I am Aditya.I am a boy.')
		self.assertEqual(response, Counter({'i': 2, 'am': 2, 'aditya': 1, 'a': 1, 'boy': 1}))

#----------------------------------------------------------------------------#

#----------------------------Main Execution----------------------------------#

if __name__ == '__main__':
	unittest.main()

#----------------------------------------------------------------------------#