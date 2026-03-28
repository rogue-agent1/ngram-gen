#!/usr/bin/env python3
"""ngram_gen - Generate n-grams from text."""
import sys, collections

def ngrams(words, n=2):
    return [tuple(words[i:i+n]) for i in range(len(words)-n+1)]

if __name__ == "__main__":
    if len(sys.argv) < 2: print("Usage: ngram_gen <file> [n] [--top N]"); sys.exit(1)
    with open(sys.argv[1]) as f: words = f.read().lower().split()
    n = int(sys.argv[2]) if len(sys.argv) > 2 else 2
    top = 20
    for i, a in enumerate(sys.argv):
        if a == "--top" and i+1 < len(sys.argv): top = int(sys.argv[i+1])
    grams = ngrams(words, n)
    counter = collections.Counter(grams)
    for gram, count in counter.most_common(top):
        print(f"{count:6d}  {' '.join(gram)}")
