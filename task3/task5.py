import collections

text = 'da da da da net net hz aaaaaaaaaaaaaaaa'.split()
longtext = max(text, key=len)
counter = collections.Counter(text).most_common(1)
print(longtext, counter[0][0])