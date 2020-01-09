num = []
get = 1
while get != 0:
    get = int(input())
    if get == 0:
        break

    a = [False, False] + [True]*(2*get-1)
    primes = []

    for i in range(2, 2*get+1):
        if a[i]:
            primes.append(i)
            for j in range(2*i, 2*get+1, i):
                a[j] = False
    count = a[get+1:].count(True)
    num.append(count)


for x in range(len(num)):
    print(num[x])