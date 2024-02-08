# 사과나무

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

res = 0
# 좌우 이동 인덱스
s = e = n//2

for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    if i < n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1

print(res)