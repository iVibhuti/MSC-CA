from collections import Counter
import json

'''
A function which creates a model, consisiting of words and their probabilities.
'''
def create_unigram_model(path):
    counts = Counter()
    probability = {}
    try:
        with open(path) as file:
            for line in file.readlines():
                line = '<s>' + line + '</s>'
                counts.update(word.strip('.,?!"\'').lower() for word in line.split())
            # return counts
        total = sum(counts.values())
        for word,count in counts.items():
            probability[word] = count / total
        # Creates a file with unigram model for the file
        with open('model', 'w') as file:
            file.write(json.dumps(probability))

    except FileNotFoundError:
        return 'File Not Found'


'''
Getting the unigram model, in a python dict format.
'''
def load_unigram_model(path_model):
    with open(path_model) as file:
        model = json.loads(file.read())
    return model
