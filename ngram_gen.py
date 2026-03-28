#!/usr/bin/env python3
"""ngram_gen - N-gram text generation and analysis."""
import sys,random,re
from collections import defaultdict
def extract_ngrams(text,n=2):
    words=re.findall(r"\w+",text.lower())
    ngrams=defaultdict(list)
    for i in range(len(words)-n):
        key=tuple(words[i:i+n]);ngrams[key].append(words[i+n])
    return ngrams
def generate(ngrams,n=2,length=50):
    key=random.choice(list(ngrams.keys()));words=list(key)
    for _ in range(length):
        if key not in ngrams:key=random.choice(list(ngrams.keys()));continue
        next_word=random.choice(ngrams[key]);words.append(next_word);key=tuple(words[-n:])
    return" ".join(words)
def top_ngrams(text,n=2,top=20):
    words=re.findall(r"\w+",text.lower())
    counts=defaultdict(int)
    for i in range(len(words)-n+1):counts[tuple(words[i:i+n])]+=1
    return sorted(counts.items(),key=lambda x:-x[1])[:top]
if __name__=="__main__":
    if len(sys.argv)<2:print("Usage: ngram_gen.py <generate|analyze> <file> [-n N]");sys.exit(1)
    cmd=sys.argv[1];text=open(sys.argv[2]).read()
    n=int(sys.argv[sys.argv.index("-n")+1]) if "-n" in sys.argv else 2
    if cmd=="generate":
        ngrams=extract_ngrams(text,n);print(generate(ngrams,n))
    elif cmd=="analyze":
        for gram,count in top_ngrams(text,n):print(f"{count:>4} {' '.join(gram)}")
