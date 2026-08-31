#!/usr/bin/env python3
"""bfgen.py — generate a Brainfuck program that prints its argument (or stdin).
Usage: python3 bfgen.py 'text'   |   echo -n 'text' | python3 bfgen.py"""
import sys
def gen(s):
    out = []; cur = 0
    for ch in s.encode():
        d = ch - cur
        out.append("+" * d if d >= 0 else "-" * (-d))
        out.append(".")
        cur = ch
    return "".join(out) + "\n"
if __name__ == "__main__":
    text = sys.argv[1] if len(sys.argv) > 1 else sys.stdin.read()
    sys.stdout.write(gen(text))
