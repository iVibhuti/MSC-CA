import re
from nltk.tokenize import RegexpTokenizer


def word_report(filename, encoding="utf-8", special_chars=None):
    counts = dict()
    tokenizer = RegexpTokenizer(r'\w+')
    try:
        with open(filename,'r',encoding=encoding) as file:
            for line in file:
                if special_chars is not None:
                    line = re.sub(special_chars,'', line)
                line = line.lower()
                words = tokenizer.tokenize(line)
                for word in words:
                    if word in counts:
                        counts[word] += 1
                    else:
                        counts[word] = 1
        return counts
    except Exception:
        return "Please check your input file!"


def generate_report(filename, word_count, unique = True, word_dct = False, get_words = False):
    unique_words = [key for key, val in word_count.items() if val is 1]
    unique_report = "Number of unique words:"+str(len(unique_words))+"\n\n"
    word_report = "Total number of words:"+str(len(word_count))+"\n\n"
    try:
        with open(filename,'w+',encoding='utf-8') as file:
            if unique and word_dct is True:
                file.write(word_report)
                file.write(unique_report)
            elif unique and get_words is True:
                file.write(unique_report)
                file.write(str(unique_words))
            elif unique is True:
                file.write(unique_report)
            elif word_dct and get_words is True:
                file.write(word_report)
                file.write(str(word_count))
            elif word_dct is True:
                file.write(word_report)
            else:
                file.write(word_report)
                file.write(str(word_count))
                file.write(unique_report)
                file.write(str(unique_words))
    except Exception:
        return "Please check the output file!"


if __name__ == "__main__":
    read_file = '../test/wiki-en-train.word'
    word_count = word_report(read_file, special_chars='(LRB|RRB)')
    write_file = './report.txt'
    generate_report(write_file, word_count, unique = False, word_dct = True, get_words = True)
