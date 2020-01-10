from collections import defaultdict
import sys
import math
import heapq

path = defaultdict(list)

N, M = map(int, sys.stdin.readline().split())

for _ in range(M):
    ed1, ed2 = map(int, sys.stdin.readline().split())
    path[ed1].append(ed2)
    path[ed2].append(ed1)

distance=[math.inf]*(N+1)
distance[1] = 0
heap = []
heapq.heappush(heap, [distance[1], 1])

while len(heap)!=0:
    [d,vertex] = heapq.heappop(heap)
    distance[vertex] = d
    
    for v in path[vertex]:
        if distance[vertex] + 1 < distance[v]:
            distance[v] = distance[vertex] + 1
            heapq.heappush(heap, [distance[v], v])
                        
max = max(distance[1:])
print(distance.index(max), max, distance.count(max))

