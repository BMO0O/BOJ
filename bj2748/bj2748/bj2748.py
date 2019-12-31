len = int(input())
f=[0, 1]
#f = [0 for _ in range(len+1)]

def FIB(A, n):
    #A[0], A[1] = 0, 1
    for i in range(n-1):
        A.append(A[i]+A[i+1])
    return A

fib = FIB(f, len)

print(fib[len])

