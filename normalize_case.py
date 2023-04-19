import sys
import argparse

def flatten(word):
    return word.lower()

def preserve(word):
    if word.isupper() or word.islower():
        return word 
    elif word[0].isupper():
        return word[0] + word[1:].lower()
    else:
        return word.lower()

parser = argparse.ArgumentParser(
        prog='normalize-case',
        description='normalize case for the words in a text file',
        epilog=''
    )   
parser.add_argument('-s', '--strategy', choices=['flatten', 'preserve'], default='preserve')
args = parser.parse_args()
action = preserve if args.strategy == 'preserve' else flatten

for line in sys.stdin:
    words = line.split()
    for i in range(len(words)):
        words[i] = action(words[i]) 
    print(" ".join(words))
