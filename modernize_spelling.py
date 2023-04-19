import sys

def case_type(word):
    if word.isupper():
        return "upper"
    elif word[0].islower():
        return "lower"
    else:
        return "capitalized"

def with_case(word, case):
    if case == "upper":
        return word.upper()
    elif case == "lower":
        return word.lower()
    else:
        return word[0].upper() + word[1:].lower()

# load lexicon into memory as dict
d = {}
with open("lexicon.txt") as f:
    for line in f:
        old, new = line.split()
        d[old] = new  

# replace each word in file
for line in sys.stdin:
    words = line.split()
    for i, word in enumerate(words):
        if word.lower() in d:
            words[i] = with_case(d[word.lower()], case_type(word)) 
    print(" ".join(words))

