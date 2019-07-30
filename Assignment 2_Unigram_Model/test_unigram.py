import math
from train_unigram import create_unigram_model, load_unigram_model

create_unigram_model('wiki-en-train.word')
model = load_unigram_model('unigram_model')

def evaluate_unigram(path):
    lambda_one = .95
    lambda_unknown = 1 - lambda_one
    W = 0
    H = 0
    unk = 0
    V = 1000000
    P = lambda_unknown / V
    with open(path) as file:
        for line in file.readlines():
            line = '<s> ' + line + '</s>'
            for word in line.split():
                W += 1
                if word in model:
                    P += lambda_one * model[word]
                else:
                    unk += 1
                    H += math.log2(P)
    return H/W , ((W-unk)/W)

'''
Calling the function & testing
'''
entropy, coverage = evaluate_unigram('wiki-en-test.word')
print('Entropy  : {}\nCoverage : {}'.format(entropy, coverage))