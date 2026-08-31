#!/usr/bin/env python3
"""bf.py — a minimal Brainfuck interpreter. Usage: python3 bf.py program.bf"""
import sys
def run(src, inp=b""):
    code = [c for c in src if c in "><+-.,[]"]
    jump = {}; stack = []
    for i, c in enumerate(code):
        if c == "[": stack.append(i)
        elif c == "]": j = stack.pop(); jump[i] = j; jump[j] = i
    tape = bytearray(30000); p = 0; i = 0; ip = 0; out = bytearray()
    while ip < len(code):
        c = code[ip]
        if   c == ">": p += 1
        elif c == "<": p -= 1
        elif c == "+": tape[p] = (tape[p] + 1) & 0xFF
        elif c == "-": tape[p] = (tape[p] - 1) & 0xFF
        elif c == ".": out.append(tape[p])
        elif c == ",": tape[p] = inp[i] if i < len(inp) else 0; i += 1
        elif c == "[" and tape[p] == 0: ip = jump[ip]
        elif c == "]" and tape[p] != 0: ip = jump[ip]
        ip += 1
    return bytes(out)
if __name__ == "__main__":
    src = open(sys.argv[1]).read() if len(sys.argv) > 1 else sys.stdin.read()
    sys.stdout.buffer.write(run(src))
