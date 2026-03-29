#!/usr/bin/env python3
"""ngram_gen - N-gram generation and frequency analysis."""
import sys, argparse, json, re
from collections import Counter

def tokenize(text):
    return re.findall(r"\b\w+\b", text.lower())

def char_ngrams(text, n):
    return [text[i:i+n] for i in range(len(text)-n+1)]

def word_ngrams(tokens, n):
    return [" ".join(tokens[i:i+n]) for i in range(len(tokens)-n+1)]

def main():
    p = argparse.ArgumentParser(description="N-gram generator")
    p.add_argument("text", help="Input text or @filename")
    p.add_argument("-n", type=int, default=2, help="N-gram size")
    p.add_argument("--type", choices=["word","char"], default="word")
    p.add_argument("--top", type=int, default=20)
    args = p.parse_args()
    text = args.text
    if text.startswith("@"):
        with open(text[1:]) as f: text = f.read()
    if args.type == "word":
        tokens = tokenize(text)
        grams = word_ngrams(tokens, args.n)
    else:
        grams = char_ngrams(text.lower(), args.n)
    freq = Counter(grams)
    top = freq.most_common(args.top)
    print(json.dumps({"n": args.n, "type": args.type, "total_ngrams": len(grams), "unique": len(freq), "top": [{"ngram": ng, "count": c} for ng, c in top]}, indent=2))

if __name__ == "__main__": main()
