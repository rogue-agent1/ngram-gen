#!/usr/bin/env python3
"""N-gram text generator."""
import sys, random, collections

def build_model(text, n=2):
    words = text.split()
    model = collections.defaultdict(list)
    for i in range(len(words) - n):
        key = tuple(words[i:i+n])
        model[key].append(words[i+n])
    return model

def generate(model, n=2, length=50, seed=None):
    if seed is not None: random.seed(seed)
    keys = list(model.keys())
    current = random.choice(keys)
    result = list(current)
    for _ in range(length):
        if current not in model: current = random.choice(keys)
        next_word = random.choice(model[current])
        result.append(next_word)
        current = tuple(result[-n:])
    return ' '.join(result)

if __name__ == '__main__':
    import argparse
    p = argparse.ArgumentParser()
    p.add_argument('file', help='Training text file')
    p.add_argument('-n', type=int, default=2, help='N-gram size')
    p.add_argument('-l', '--length', type=int, default=50)
    p.add_argument('-s', '--seed', type=int)
    args = p.parse_args()
    text = open(args.file).read()
    model = build_model(text, args.n)
    print(generate(model, args.n, args.length, args.seed))
