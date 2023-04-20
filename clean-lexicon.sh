#!/bin/sh
# Sort and de-duplicate lexicon file
cat lexicon.txt | sort | uniq > tmp.txt
cp tmp.txt lexicon.txt
rm tmp.txt
wc -l lexicon.txt
