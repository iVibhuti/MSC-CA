import io
import argparse
from collections import Counter
import json

def openfile(filename):
    strh = ''
    try:
        fh = open(filename, encoding="utf8") 
        strh = fh.readlines()
        return True, strh
    except Exception:
        return False,strh

#def train_bigram(training_file, model_file):
def train_bigram(filename):
    counts = Counter()
    context_counts = Counter()
    status, file = openfile(filename)
    try:
        for line in file:
            token = line.strip().split(' ')
            token.insert(0, '<s>')
            token.append('</s>')
            for i in range(1, len(token)): # starting at 1, after <s>
                    # Add bigram and bigram context.
                    counts[' '.join(token[i-1:i+1])] += 1  # Number of 'w_i, w_{i-1}'
                    context_counts[token[i-1]] += 1  # Number of w_{i-1}.
                    # Add unigram and unigram context.
                    counts[token[i]] += 1  # Number of w_i.
                    context_counts[''] += 1  # Total number of words.
    except FileNotFoundError:
        return 'File Not Found'
    probabilities = {}
    for ngram, count in sorted(counts.items(),key=lambda x:x[1],reverse=True):
        words = ngram.split(' ')
        context = words[:-1]
        context = ' '.join(context)
        probabilities[ngram] = count / context_counts[context]
        # Creates a file with bigram model for the file
        with open('model.json', 'w') as file:
            file.write(json.dumps(probabilities))