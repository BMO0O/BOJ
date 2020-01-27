N = int(input())

die = list(map(int, input().split()))

sum3 = [die[0]+die[1]+die[2], die[0]+die[1]+die[3], die[0]+die[2]+die[4], die[0]+die[3]+die[4], die[5]+die[1]+die[2], die[5]+die[1]+die[3], die[5]+die[4]+die[3], die[5]+die[4]+die[2]]

if N>=2:
    dice = []
    for i in range(6):
        dice.append((die[i], i))

    dice.sort(reverse = True)
    (x,y) = dice.pop()
    (a,b) = dice.pop()
    if y+b==5:
        (a,b) = dice.pop()
    get = x+a
    
    result = min(sum3)*4 + (4*(N-2)+4*(N-1))*get + ((N-2)*(N-2)+(N-1)*(N-2)*4)*min(die)
    print(result)

else:
    die.sort()
    print(sum(die[:5]))

