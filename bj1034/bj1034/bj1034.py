
N, M = map(int, input().split())

table = [[0 for i in range(M)] for j in range(N)]

(max, index) = (0, 0)

for x in range(N):
    lamp = input()
    table[x] = lamp

K = int(input())

pos = []

for col in range(N):
    count = table[col].count('0')
    if count<=K and count%2 == K%2: pos.append(table[col])

for i in range(len(pos)):
    if max < table.count(pos[i]):
        max = table.count(pos[i])

print(max)
