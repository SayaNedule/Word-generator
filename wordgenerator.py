
from nltk.tokenize import WhitespaceTokenizer
import nltk
from collections import Counter
import random

with open(input(), "r", encoding="utf-8") as corpus:
    tokens = WhitespaceTokenizer().tokenize(corpus.read())
    bigrm = list(nltk.trigrams(tokens))
    trigrams = []
    tries = []
    for h in bigrm:
        head = h[0] + ' ' + h[1]
        tries.append(head)
    for trig in bigrm:
        new_list = []
        head = trig[0] + ' ' + trig[1]
        tail = trig[2]
        new_list.append(head)
        new_list.append(tail)
        trigrams.append(new_list)
    probabilities = Counter(bigrm).most_common()
for sentence in range(10):
    while True:
        token = str(random.choice(tries))
        a = token.split()
        if a[0][0].isupper() is True and a[0][-1] not in ".?!":
            break
    sentence = []
    sentence.append(a[0])
    sentence.append(a[1])
    cond = True
    while True:
        if len(sentence) >= 5 and sentence[-1][-1] in ".!?":
            break
        else:
            a_list = []
            for k in trigrams:
                if k[0] == token:
                    a_list.append(k)
            a = max(a_list)
            tail = a[1]
            sentence.append(tail)
            conv = token.split()
            token = conv[1] + ' ' + tail
    print(" ".join(sentence))
