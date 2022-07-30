import pprint

text = 'ananas'

counts = dict()
for word in text:
    if word in counts.keys():
        counts[word] += 1
    else:
        counts[word] = 1

pprint.pprint(counts)