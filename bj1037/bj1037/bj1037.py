T = int(input())

factors = list(map(int, input().split()))

factors.sort()

N = factors[0]*factors[T-1]
print(N)