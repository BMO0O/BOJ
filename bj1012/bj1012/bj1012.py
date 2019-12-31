import queue


def BFS(G, came_from, v):
    Q = queue.Queue()
    Q.put(v)

    while Q.qsize() > 0:
        current = Q.get()

        (x, y) = current
        candidates = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        for next in [(h, v) for h,v in candidates if G[v][h] != 0]:
            if next not in came_from:
                Q.put(next)
                came_from.append(next)
    return came_from


T = int(input())
result = []

for _ in range(T):
    M, N, K = map(int, input().split())
    farm = [[0]*(M+2) for _ in range(N+2)]
    visited = []
    cabbage = []
    earthworm = 0
    
    for _ in range(K):
        i, j = map(int, input().split())
        farm[j+1][i+1] = 1
        cabbage.append((i+1, j+1))
    

    for x in cabbage:
        if x not in visited:
            visited = BFS(farm, visited, x)
            earthworm = earthworm + 1

    result.append(earthworm)

for num in range(T):
    print(result[num])
