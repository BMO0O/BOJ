import math
import sys

T = int(sys.stdin.readline())
result = []

for _ in range(T):
    a, b = map(int, sys.stdin.readline().split())
    
    
    if a == 1:
        result.append(1)
    elif a == 5:
        result.append(5)
    elif a == 6:
        result.append(6)

    else:
        repeat = []
        temp = 1
        for _ in range(b):
            temp = temp*a
            temp = temp%10
            if temp in repeat:
                result.append(repeat[b%len(repeat)-1])
                break
            repeat.append(temp)

    

for i in range(T):
    if result[i] == 0:
        print(10)
    else:
        print(result[i])
