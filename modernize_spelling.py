import sys

punct = {',', '.', ':', ';', '?', '!', '(', ')'}

# i is the first non-punct, j is first end punct
def split_punct(word):
    i = 0
    while i < len(word) and word[i] in punct:
        i += 1
    j = len(word)
    while j > 0 and word[j-1] in punct:
        j -= 1
    return (word[:i], word[i:j], word[j:]) if word[i:j] else (word[:i], '', '')

# load lexicon into memory as dict
d = {}
with open("lexicon.txt") as f:
    for line in f:
        k, v = line.split()[:2]
        d[k] = v  

# replace each word in file
for line in sys.stdin:
    words = line.split()
    for i in range(len(words)):
        lpunct, word, rpunct = split_punct(words[i])
        print(lpunct, end='')
        print(d[word] if word in d else word, end='')
        print(rpunct, end=' ')
    print()

