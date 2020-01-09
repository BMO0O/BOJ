import sys

A, B, C = map(int, sys.stdin.readline().split())

if B>=C:
    print(-1)
else:
    result = A/(C-B) + 1
    print(int(result))
