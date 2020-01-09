T = int(input())

a = [False, False] + [True]*(10000-1)
golden = []   
for i in range(2, 10001):
    if a[i]:
        for j in range(2*i, 10001, i):
            a[j] = False

for _ in range(T):
    num = int(input())
    if a[int(num/2)]: golden.append((num/2, num/2))
    else:
        for i in range(int(num/2), num+1):
            if a[i]:
                if a[num-i]:
                    golden.append((num-i, i))
                    break

for i in range(T):
    x, y = map(int, golden[i])
    print(x, y)

    





