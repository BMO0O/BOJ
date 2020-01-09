from itertools import accumulate
from operator import xor

T = int(input())


count = []


for i in range(T):
    X_s, Y_s, X_g, Y_g = map(int, input().split())
    PLANET = int(input())
    Start = []
    Goal = []
    result = []

    for _ in range(PLANET):
        Xc, Yc, R = map(int, input().split())
        if (X_s - Xc)**2+(Y_s-Yc)**2<R**2:
            Start.append(1)
        else:
            Start.append(0)
        if (X_g - Xc)**2+(Y_g-Yc)**2<R**2:
            Goal.append(1)
        else:
            Goal.append(0)

    result = [int(Start[i])^int(Goal[i]) for i in range(PLANET)]

    count.append(sum(result))

for i in range(T):
    print(count[i])



        
