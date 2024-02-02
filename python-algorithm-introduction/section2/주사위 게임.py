# 주사위 게임

from itertools import combinations as cb

# 참여하는 사람 수
n = int(input())

res = 0

for i in range(n):
    tmp = input().split()
    tmp.sort()
    # 일대일 대응
    a,b,c = map(int, tmp) 
    if (a == b) and (b == c):
        money = 10000 + (a*1000)

    elif (a == b) or (a == c):
        money = 1000 + (a*100)
    
    elif (b == c):
        money = 1000 + (b*100)

    else:
        # 오른차순 정렬했으므로 c가 가장 큰 수
        money = c*100

    if money > res:
        res = money

print(res)    