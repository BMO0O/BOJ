import queue

N, M = map(int, input().split())

maze = [[0]*(M+2) for _ in range(N+2)]

for i in range(1,N+1):
    s = [0]+list(map(int,list(input())))+[0]
    maze[i] = s
maze[i+1] = [0]*(M+2)


start = (1, 1)
goal = (M, N)
Q = queue.Queue()
Q.put(start)
came_from = {}


while Q.qsize() > 0:
    current = Q.get()

    if current == goal:
        break

    (x, y) = current
    candidates = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    for next in [(h, v) for h,v in candidates if maze[v][h] != 0]:
        if next not in came_from:
            Q.put(next)
            came_from[next] = current

current = goal
path = []

while current is not start:
    path.append(current)
    current = came_from[current]

print(len(path)+1)

