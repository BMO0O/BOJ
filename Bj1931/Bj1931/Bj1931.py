import sys
L = int(input())
#sch = [[0 for j in range(2)]for i in range(L)]
#sch = [[int(x) for x in input().split()] for y in range(L)]
sch = sorted([list(map(int, sys.stdin.readline().split())) for i in range(L)], key = lambda x: (x[1], x[0])) 


def Greedy_schedule(A, n):
    T = []
    T.append(A[0])
    last = T[0]
    answer = 1;
    for i in range(1, n):
      if last[1] <= A[i][0]:
        T.append(A[i])
        last = A[i]
        answer = answer + 1;
        
    return answer


print(Greedy_schedule(sch, L))

