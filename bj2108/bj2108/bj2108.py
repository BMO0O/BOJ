from collections import Counter
import sys

T = int(sys.stdin.readline())

num = [0] * T

for i in range(T):
    num[i] = int(sys.stdin.readline())

num.sort()
cnt = Counter(num)
cnt = cnt.most_common(2)

print(round(sum(num)/T))
print(num[int(T/2)])
if len(cnt)>1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
    
print(num[len(num)-1]-num[0])