from collections import Counter
def main():
    with open(r'./wiki-en-train.word',encoding="utf8") as f:
        words = [word for line in f for word in line.split()]
        print("The total number of words count is: ",len(words))
        c = Counter(words)
        for word, count in c.most_common():
            print(word,count)
main()









    
