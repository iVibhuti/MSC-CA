"""
NAME: Shubham Kumar
PRN: 18030142032
PROGRAM: MSc. C.A.(DS)
"""
import re
import math
import pickle

# Loding Model File
def load_model(model_file):
    with open(model_file, 'rb') as file:
        probabilities = pickle.load(file)
    return probabilities

# Testing Unigram Models
def test_unigram(probabilities, test_file):
    sentence_lst = list()
    LAMBDA_1 = 0.95
    LAMBDA_UNK = 1 - LAMBDA_1
    V = 1e6  # Vocabulary size.
    W = 0  # Total number of words.
    unk = 0  # Number of unknown words. (for calculating coverage.)
    H = 0  # Negative log likelihood.

    with open(test_file, 'r',encoding='utf-8') as file:
        for line in file:
            line = re.sub(r'(-LRB-|-RRB-|\/|`|\'|\\)','', line)
            m = re.split(r'(?<=[^A-Z].[.?]) +(?=[A-Z])', line)
            for i in m:
                sentence = '<s>'+ i + '</s>'
                sentence_lst.append(sentence.replace('\n',''))
    for word in sentence_lst:
        W += 1
        P = LAMBDA_UNK / V
        if word in probabilities:
            P += LAMBDA_1 * probabilities[word]
        else:
            unk += 1
        H += - math.log2(P)
    # Entropy H is average negative log2 likelihood per word.
    print('Entropy: {}'.format(H / W))
    # Coverage is the percentage of known words in the corpus.
    print('Coverage: {}'.format((W - unk)/W))


if __name__ == "__main__":
    model_file = './unigram.model'
    test_file = '../test/wiki-en-test.word'
    print("---LOADING MODEL---")
    model = load_model(model_file)
    print("---TESTING MODEL---")
    test_unigram(model,test_file)