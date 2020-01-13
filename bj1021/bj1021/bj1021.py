N, M = map(int, input().split())

num = list(map(int, input().split()))
queue = [i for i in range(1,N+1)]
current = 1
sum = 0

for _ in range(M):
    L = len(queue)

    if queue.index(num[0]) > queue.index(current):
        right = L - queue.index(num[0]) + queue.index(current)
        left = queue.index(num[0]) - queue.index(current)
        if right < left:
            sum += right
        else:
            sum += left
    elif queue.index(num[0]) < queue.index(current):
        right = L - queue.index(current) + queue.index(num[0])
        left = queue.index(current) - queue.index(num[0])
        if right < left:
            sum += right
        else:
            sum += left
    current = queue[(queue.index(num[0])+1)%L]
    queue.remove(num[0])
    del num[0]

print(sum)

    