from collections import Counter

# Opening the file
def open_file(location , file = ''):
    try:
        file = open(location , 'r')
        return True, file
    except Exception:
        return False, file

# Closing the file
def close_file(file):
    try:
        file.close()
        return True
    except Exception:
        return False

# Function to keep count of each word of the text
def occurence_count(text):
    counts = Counter()
    counts.update(word.strip('.,?!"\'').lower() for word in text.split())
    return counts

# main
flag , file = open_file('wiki-en-train.word')
if flag:
    # print(file.read())
    # for key , value in occurence_count(file.read()).items():
    #     print(key, value) '''
    # print(occurence_count('Tejas Tejas is a Boy,? boY.'))
    print(occurence_count(file.read()))
    close_file(file)
else:
    print('Something went wrong while reading the file.')
