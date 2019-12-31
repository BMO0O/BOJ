import math

N, M = map(int, input().split())

getmap = [[0]*M for i in range(N)]
whiteFirst = [
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
];

blackFirst = [
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
        [ 'B','W','B','W','B','W','B','W' ],
        [ 'W','B','W','B','W','B','W','B' ],
];

for i in range(N):
    s = list(input())
    getmap[i] = s

cut = []

result = math.inf
cnt1 = 0
cnt2 = 0

for i in range(N-7):
    for j in range(M-7):
        for a in range(8):
            for b in range(8):
                if(getmap[i+a][j+b]!=whiteFirst[a][b]):
                    cnt1= cnt1+1;
                if(getmap[i+a][j+b]!=blackFirst[a][b]):
                    cnt2 = cnt2+1;
                
        result = min(result, cnt1, cnt2)
        cnt1 = 0
        cnt2 = 0



print(result)