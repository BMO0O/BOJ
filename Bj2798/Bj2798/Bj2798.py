import math

n, m = map(int, input().split())

num = list(map(int, input().split()))
sorted_num = sorted(num)
L = len(num)

def Max_sum(A):
    s = list(range(n));
    maxsum = -math.inf;
    i = 0;
    while i<n:
        if(i-1<0):
            s[i] = A[i];
            if maxsum < s[i]:
                maxsum, s[i] = A[i], A[i];
                maxi, maxj = i, i;
            i = i+1;
        else:
            s[i]=s[i-1]+A[i];
            if maxsum < s[i]:
                if s[i-1] < 0:
                    maxsum, s[i] = A[i], A[i];
                    maxi, maxj = i, i;
                else:
                    maxsum, maxj = s[i], i;
            i = i+1;
    return maxsum;

def Blackjack(A):
    answer = 0 
    i = 0
    for i in range(0, L-2):
        for j in range(i+1, L-1):
            for k in range(j+1, L):
                if A[i]+A[j]+A[k]<=m and A[i]+A[j]+A[k]>answer:
                    answer = A[i]+A[j]+A[k];
    return answer


#print(Max_sum(sorted_num));
print(Blackjack(num))


