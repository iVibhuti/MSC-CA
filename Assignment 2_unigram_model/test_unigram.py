'''
Name : Abhishek Anand
Prn  : 18030142002
PROGRAM:	MSC-CA (Data Science)
Symbiosis Institute of Computer Studies and Research, Pune
'''
import math
from unigram import unigram_model, load_unigram_model

unigram_model('wiki-en-train.word')
model = load_unigram_model('model_unigram')

def calculate_unigram(filename):
    lambda_1 = .95
    lambda_new = 1 - lambda_1
    W = 0
    H = 0
    unk = 0
    V = 1000000
    P = lambda_new / V
    with open(filename) as file:
        for line in file.readlines():
            line = '<s> ' + line + '</s>'
            for word in line.split():
                W += 1
                if word in model:
                    P += lambda_1 * model[word]
                else:
                    unk += 1
                    H += math.log2(P)
    return H/W , ((W-unk)/W)


entropy, coverage = calculate_unigram('wiki-en-test.word')
print('Entropy  : {}\nCoverage : {}'.format(entropy, coverage))
