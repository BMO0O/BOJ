from collections import defaultdict
import queue

N, M, V = map(int, input().split())

path = defaultdict(list)
visited = []

for _ in range(M):
    ed1, ed2 = map(int, input().split())
    if ed2 not in path[ed1]:
        path[ed1].append(ed2)
    if ed1 not in path[ed2]:
        path[ed2].append(ed1)

for i in range(1,N+1):
    if i not in path.keys():
        path[i]=[]

for i in path.keys():
    path[i] = sorted(path[i])


##DFS IMPLEMENT

def DFS(G,visit,v):
    visit.append(v)
    for x in G[v]:
        if x not in visit:
            DFS(G,visit,x)
    return visit

##BFS IMPLEMENT

def BFS(G, v):
    came_from= []
    Q = queue.Queue()
    came_from.append(v)
    Q.put(v)
    
    while Q.qsize() > 0:
        current=Q.get()
        for x in G[current]:
            if x not in came_from:
                came_from.append(x)
                Q.put(x)

    return came_from

visited = DFS(path, visited, V)
print(*visited, sep=' ')

visited = BFS(path, V)
print(*visited, sep=' ')
 