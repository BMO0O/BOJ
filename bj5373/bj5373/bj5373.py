


def rotate_90(M):
    N = len(M)
    
    temp = [[0]*N for _ in range(N)]
    
    for r in range(N):
        for c in range(N):
            temp[c][N-1-r] = M[r][c]

    return temp

def rotate_270(M):
    N = len(M)

    temp = [[0]*N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            temp[N-1-c][r] = M[r][c]
    return temp


class CUBE(object):
    def __init__(self):
        self.U = ([['w' for col in range(3)] for row in range(3)])
        self.D = ([['y' for col in range(3)] for row in range(3)])
        self.F = ([['r' for col in range(3)] for row in range(3)])
        self.B = ([['o' for col in range(3)] for row in range(3)])
        self.L = ([['g' for col in range(3)] for row in range(3)])
        self.R = ([['b' for col in range(3)] for row in range(3)])

    def turn(self, pos, op):
        temp_U = [0 for i in range(3)]
        temp_D = [0 for i in range(3)]
        temp_F = [0 for i in range(3)]
        temp_B = [0 for i in range(3)]
        temp_L = [0 for i in range(3)]
        temp_R = [0 for i in range(3)]
        
        if pos == 'U':
            if op == '-':
                for i in range(3):
                    self.B[0][i], self.R[0][i], self.F[0][i], self.L[0][i] = self.R[0][i], self.F[0][i], self.L[0][i], self.B[0][i]
                self.U = rotate_270(self.U)

            if op == '+':
                for i in range(3):
                    self.B[0][i], self.R[0][i], self.F[0][i], self.L[0][i] = self.L[0][i], self.B[0][i], self.R[0][i], self.F[0][i]
                self.U = rotate_90(self.U)

        elif pos == 'D':
            if op == '-':
                for i in range(3):
                    self.B[2][i], self.R[2][i], self.F[2][i], self.L[2][i] = self.L[2][i], self.B[2][i], self.R[2][i], self.F[2][i]
                self.D = rotate_270(self.D)

            if op == '+':
                for i in range(3):
                    self.B[2][i], self.R[2][i], self.F[2][i], self.L[2][i] = self.R[2][i], self.F[2][i], self.L[2][i], self.B[2][i]
                self.D = rotate_90(self.D)

        elif pos == 'F':
            if op == '+':
                for i in range(3):
                    temp_U[i], temp_R[i], temp_D[i], temp_L[i] = self.L[i][2], self.U[2][2-i], self.R[i][0], self.D[0][i]
                    #self.U[2][2-i], self.R[i][0], self.D[0][2-i], self.L[i][2] = self.L[i][2], temp_U[2][2-i], self.R[i][0], self.D[0][i]
                for i in range(3):
                    self.U[2][i] = temp_U[2-i]
                    self.R[i][0] = temp_R[2-i]
                    self.D[0][i] = temp_D[2-i]
                    self.L[i][2] = temp_L[i]
                self.F = rotate_90(self.F)    
            if op == '-':
                for i in range(3):
                    temp_U[i], temp_R[i], temp_D[i], temp_L[i] = self.R[i][0], self.D[0][i], self.L[i][2], self.U[2][2-i]
                    #self.U[2][2-i], self.R[i][0], self.D[0][i], self.L[i][2] = self.R[i][0], self.D[0][i], self.L[i][2], temp_U[2][2-i]
                for i in range(3):
                    self.U[2][i] = temp_U[i]
                    self.R[i][0] = temp_R[2-i]
                    self.D[0][i] = temp_D[i]
                    self.L[i][2] = temp_L[i]
                self.F = rotate_270(self.F)

        elif pos == 'B':
            if op == '+':
                for i in range(3):
                    temp_D[i], temp_R[i], temp_U[i], temp_L[i]  = self.L[i][0], self.D[2][2-i], self.R[i][2], self.U[0][2-i] 
                    #self.D[2][i], self.R[i][2], self.U[0][i], self.L[i][0]  = self.L[i][0], self.D[2][2-i], temp_R[i][2], temp_U[0][2-i] 
                for i in range(3):
                    self.D[2][i] = temp_D[i]
                    self.R[i][2] = temp_R[i]
                    self.U[0][i] = temp_U[i]
                    self.L[i][0] = temp_L[i]
                self.B = rotate_90(self.B)
                
            if op == '-':
                for i in range(3):
                    temp_U[i], temp_R[i], temp_D[i], temp_L[i] = self.L[2-i][0], self.U[0][i], self.R[i][2], self.D[2][i]
                    #self.U[0][i], self.R[i][2], self.D[2][i], self.L[2-i][0] = temp_L[2-i][0], self.U[0][i], self.R[i][0], self.D[2][i]
                for i in range(3):
                    self.D[2][i] = temp_D[2-i]
                    self.R[i][2] = temp_R[i]
                    self.U[0][i] = temp_U[i]
                    self.L[i][0] = temp_L[i]

                self.B = rotate_270(self.B)

        elif pos == 'L':
            if op == '+':
                for i in range(3):
                    temp_U[i], temp_F[i], temp_D[i], temp_B[i] = self.B[2-i][2], self.U[i][0], self.F[i][0], self.D[i][0]
                    #self.U[i][0], self.F[i][0], self.D[i][0], self.B[2-i][2] = self.B[2-i][2], self.U[i][0], self.F[i][0], self.D[i][0]
                for i in range(3):
                    self.U[i][0] = temp_U[i]
                    self.F[i][0] = temp_F[i]
                    self.D[i][0] = temp_D[i]
                    self.B[2-i][2] = temp_B[i]
                self.L = rotate_90(self.L)
            if op == '-':
                for i in range(3):
                    temp_U[i], temp_F[i], temp_D[i], temp_B[i] = self.F[i][0], self.D[i][0], self.B[2-i][2], self.U[i][0]
                    #self.U[i][0], self.F[i][0], self.D[i][0], self.B[2-i][2] = self.F[i][0], self.D[i][0], self.B[2-i][2], self.U[i][0]
                for i in range(3):
                    self.U[i][0] = temp_U[i]
                    self.F[i][0] = temp_F[i]
                    self.D[i][0] = temp_D[i]
                    self.B[2-i][2] = temp_B[i]
                self.L = rotate_270(self.L)

        elif pos == 'R':
            if op == '+':
                for i in range(3):
                    temp_B[i], temp_D[i], temp_F[i], temp_U[i] = self.U[i][2], self.B[i][0], self.D[i][2], self.F[i][2]
                    #self.B[i][2], self.D[i][2], self.F[i][2], self.U[i][2] = self.U[i][2], self.B[i][2], self.D[i][2], self.F[i][2]
                for i in range(3):
                    self.B[i][0] = temp_B[2-i]
                    self.D[i][2] = temp_D[2-i]
                    self.F[i][2] = temp_F[i]
                    self.U[i][2] = temp_U[i]

                self.R = rotate_90(self.R)
            if op == '-':
                for i in range(3):
                    temp_B[i], temp_D[i], temp_F[i], temp_U[i] = self.D[i][2], self.F[i][2], self.U[i][2], self.B[i][0]
                    #self.B[i][2], self.D[i][2], self.F[i][2], self.U[i][2] = self.D[i][2], self.F[i][2], self.U[i][2], self.B[i][2]
                for i in range(3):
                    self.B[i][2] = temp_B[2-i]
                    self.D[i][2] = temp_D[i]
                    self.F[i][2] = temp_F[i]
                    self.U[i][2] = temp_U[i]

                self.R = rotate_270(self.R)
    
    
T = int(input())   

result = []

for _ in range(T):
    N = int(input())
    cube = CUBE()
    
    
    turn = list(input().split())
    
    for M in turn[:N]:
        order = list(M)
        cube.turn(order[0], order[1])

    #result.append(cube.U)
    for i in range(3):
        for j in range(3):
            print(cube.U[i][j], end='')
        print('')
    for i in range(3):
        for j in range(3):
            print(cube.B[i][j], end='')
        print('')
    for i in range(3):
        for j in range(3):
            print(cube.D[i][j], end='')
        print('')
    for i in range(3):
        for j in range(3):
            print(cube.F[i][j], end='')
        print('')
    for i in range(3):
        for j in range(3):
            print(cube.L[i][j], end='')
        print('')
    for i in range(3):
        for j in range(3):
            print(cube.R[i][j], end='')
        print('')
    
    
#for i in result:
#    for x in range(3):
#        for y in range(3):
#            print(i[x][y], end='')
#        print('')
        
    

