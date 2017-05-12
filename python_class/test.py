


words = ['why','are','you','not','looking','in','my','eyes']

from collections import Counter
word_counts = Counter(words)

for word in words:
    word_counts[word] += 1

print(word_counts)