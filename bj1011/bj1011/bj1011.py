import math

T = int(input())
result = []
for _ in range(T):
    X, Y = map(int, input().split())

    distance = Y - X
    i = 1
    while i*i <= Y - X:
        i += 1
    i -= 1
    warp = math.ceil((distance - i*i)/i)
    warp = warp + 2*i - 1
    result.append(warp)

    
    
for j in range(T):
    print(result[j])







