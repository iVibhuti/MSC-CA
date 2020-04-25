import io
import argparse
import math

V = 1e6  # Vocabulary size.

def load_model(modelfile):
    with open(modelfile) as file:
        model = json.loads(file.read())
    return model

def test_bigram(lambdaval,probs, test_file):
        lambda_1 = lambdaval
        lambda_2 = 1 - lambda_1
        W = 0  # Total number of words.
        H = 0  # Negative log likelihood.
        with open(test_file, 'r') as f:   
            for line in f:
                words = line.strip().split(' ')
                words.insert(0, '<s>')
                words.append('</s>')
                for i in range(1, len(words)):
                    try:
                        P1 = lambda_1 * probs[words[i]] + (1 - lambda_1) / V
                        P2 = lambda_2 * probs[' '.join(words[i-1:i+1])] + (1 - lambda_2) * P1
                        H += - math.log2(P2)
                        W += 1
                        print('Entropy is : {}'.format(H/W))
                    except:
                        print('This words sequence is not in training data thaswhy the probability of theses coming together is zero.')
                        