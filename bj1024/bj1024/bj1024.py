
N, L = map(int, input().split())

x = 0

for i in range(L, 101):
    x = N/i - (i-1)/2
    if int(x) == x and x >=0 :
        seq = [j for j in range(int(x), int(x)+i)]
        print(*seq)
        break
    if ((i-1)*i)/2 > N or i == 100:
        print(-1)
        break

