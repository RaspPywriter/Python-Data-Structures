
#using Counter to get counts of most common words
from collections import Counter
wordList = [
   'red', 'green', 'black', 'pink', 'black', 'white', 'black', 'eyes',
   'white', 'black', 'orange', 'pink', 'pink', 'red', 'red', 'white', 'orange',
   'white', "black", 'pink', 'green', 'green', 'pink', 'green', 'pink',
   'white', 'orange', "orange", 'red'
]

count = Counter(wordList)
top = count.most_common(4)
print(top)

#using dictionary to get counts of most common words
counts = dict()
for line in wordList:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1

for keys,values in counts.items():
    print(keys)
    print(values)


