"""
NAME: Shubham Kumar
PRN: 18030142032
PROGRAM: MSc. C.A.(DS)

Assignment 2 : To create unigram model and calculate entropy & coverage.
"""

import re

import re
import pickle

def train_unigram(training_file):
    counts = dict()
    total_count = 0
    sentence_lst = list()
    unigram_model = dict()
    words = list()

    def word_count(line):
        try:
            token = re.compile(r'\w+')
            words.extend(token.findall(line.lower()))
            for word in words:
                if word in counts:
                    counts[word] += 1
                else:
                    counts[word] = 1
            return counts
        except Exception as e:
            print(e)

    with open(training_file, 'r', encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'(-LRB-|-RRB-|\/|`|\'|\\)', '', line)
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', line)
            for i in m:
                sentence = '<s>' + i + '</s>'
                sentence_lst.append(sentence.replace('\n', ''))

    for line in sentence_lst:
        word_count(line)
    s = counts.get('s') // 2
    slash_s = counts.get('s') // 2
    counts.pop('s')
    for x in counts.keys():
        total_count += counts.get(x)
    total_count += s + slash_s
    for x in counts.keys():
        probability = counts.get(x) / total_count
        unigram_model[x] = probability
    print("MODEL CREATED SUCCESSFULLY!")
    return unigram_model


if __name__ == "__main__":
    print("---CREATING UNIGRAM MODEL---")
    train_file = '../test/wiki-en-train.word'
    model_file = "./unigram.model"
    model = train_unigram(train_file)
    print("---Saving Model---")
    with open(model_file, 'wb') as file:
        pickle.dump(model, file)
    print("MODEL SAVED SUCCESSFULLY!")