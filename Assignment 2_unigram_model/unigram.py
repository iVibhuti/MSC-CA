'''
Name : Abhishek Anand
Prn  : 18030142002
PROGRAM:	MSC-CA (Data Science)
Symbiosis Institute of Computer Studies and Research, Pune
'''
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

def unigram_model(filename):
    counts = Counter()
    probability = {}
    status, file = openfile(filename)
    try:
        for line in file:
            line = '<s>' + line + '</s>'
            counts.update(word.strip('.,?!"\'').lower() for word in line.split())
        total_count = sum(counts.values())
        for word,count in counts.items():
            probability[word] = count / total_count
        # Creates a file with unigram model for the file
        with open('model_unigram', 'w') as file:
            file.write(json.dumps(probability))

    except FileNotFoundError:
        return 'File Not Found'

def load_unigram_model(modelfile):
    with open(modelfile) as file:
        model = json.loads(file.read())
    return model