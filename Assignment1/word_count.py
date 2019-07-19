"""
NAME: Shubham Kumar
PRN: 18030142032
PROGRAM: MSc. C.A.(DS)
"""

import re


class WordCount:

    def __init__(self):
        self.counts = dict() # Word dictionary for the given input. Ex: {'a':1}
        self.words = list() # Get word list for the given input.

    # Count the words in for the given lines and update it to dictionary.
    def word_count(self, line):
        try:
            token = re.compile(r'\w+')
            self.words.extend( token.findall(line.lower()) )
            # words = self.tokenizer.tokenize(line.lower())
            for word in self.words:
                if word in self.counts:
                    self.counts[word] += 1
                else:
                    self.counts[word] = 1
            return self.counts
        except Exception as e:
            print(e)

    # Generate the word count dictionary for the given file.
    # Arguments List :-
    #   filename: name of the file.
    #   encoding: file encoding. Default "UTF-8"
    #   special_chars: special characters other than symbols which are needed to be removed.
    #       Ex:- "This is a --LRB--TEST--RRB". Here --LRB-- & --RRB-- are parenthesis in the given line.
    def word_report(self, filename, encoding="utf-8", special_chars=None):
        try:
            with open(filename, 'r', encoding=encoding) as file:
                # Reading file line by line and updating the dictionary.
                for line in file:
                    if special_chars is not None:
                        line = re.sub(special_chars, '', line)
                    self.word_count(line)
            return self.counts
        except Exception as e:
            print(e)
            return "Please check your input file!"

    # Generate word report for the given file.
    # Arguments List :-
    #   filename: name of the file where the report is going to be stored.
    #   word_count: dictionary generated from word report.
    #   unique: report of the unique words. Default 'True'.
    #   word_dct: report of all words present in the dictionary. Default 'False'.
    #   get_words: get the word dictionary output in the report. Default 'False'.
    def generate_report(self, filename, word_count, unique=True, word_dct=False, get_words=False):
        unique_words = [key for key, val in word_count.items() if val is 1]
        unique_report = "Number of unique words:" + str(len(unique_words)) + "\n\n"
        word_report = "Total number of words:" + str(len(word_count)) + "\n\n"
        try:
            with open(filename, 'w+', encoding='utf-8') as file:
                if unique and word_dct is True:
                    file.write(word_report)
                    file.write(unique_report)
                elif unique and get_words is True:
                    file.write(unique_report)
                    file.write(str(unique_words))
                elif unique is True:
                    file.write(unique_report)
                elif word_dct and get_words is True:
                    file.write(word_report)
                    file.write(str(word_count))
                elif word_dct is True:
                    file.write(word_report)
                else:
                    file.write(word_report)
                    file.write(str(word_count))
                    file.write(unique_report)
                    file.write(str(unique_words))
        except Exception as e:
            print(e)
            return "Please check the output file!"


if __name__ == "__main__":
    wc = WordCount()
    read_file = '../test/wiki-en-train.word'
    word_count = wc.word_report(read_file, special_chars='(LRB|RRB)')
    print("Word_Report Count:", len(word_count))
    write_file = './report.txt'
    wc.generate_report(write_file, word_count, unique=False, word_dct=False, get_words=True)
