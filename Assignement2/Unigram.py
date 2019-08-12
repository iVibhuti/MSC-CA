#!/usr/bin/env python
# coding: utf-8

'''Name- Abhinav Anil
    PRN -18030142001
'''    


from collections import Counter
counts = Counter()
with open('wiki-en-train.word', encoding='utf-8') as file:
    for line in file.readlines():
        line = '<s> ' + line + ' </s>'
        counts.update(word.strip('.,?!"\'').lower() for word in line.split())



total_count = sum(counts.values())

probability = {}
for word,count in counts.items():
    probability[word] = count / total_count




import json
with open('model', 'w') as file:
     file.write(json.dumps(probability)) # use `json.loads` to do the reverse



'''Loading the model'''

with open('model.txt') as file:
    probability = json.loads(file.read())

lambda_one = .95
lambda_unknown = 1 - lambda_one
W = 0
H = 0
unk = 0
V = 1000000
P = lambda_one / V
unknown = {}


'''Test Unigram'''

import math

with open('wiki-en-test.word',encoding='utf-8') as file:
    for line in file.readlines():
        line = '<s> ' + line + '</s>'
        for word in line.split():
            W += 1
            if word in probability:
                P += lambda_one * probability[word]
            else:
                unk += 1
                H += math.log2(P)



'''Entropy'''
H/W


'''Coverage'''
(W-unk) / W

def ngram(n , text):
    nlist = []
    for i in range(len(text.split()) - (n - 1)):
        nlist.append(text.split()[i : i + n])
    return nlist


print(ngram(2 , 'Abhinav Anil Verma a'))






