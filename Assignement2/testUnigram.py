import math
from trainUnigram import create_unigram_model, load_unigram_model
'''
Calling functions from train file to create and load model
'''
create_unigram_model('wiki-en-train.word',encoding='utf-8')
model = load_unigram_model('model')

'''
After we read the model here, testing it against the testing data file,
and getting entropy and coverage of the unigrams.
'''
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
entropy, coverage = evaluate_unigram('.wiki-en-test.word')
print('Entropy  : {}\nCoverage : {}'.format(entropy, coverage))
