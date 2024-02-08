# 곶감 모래시계

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    # 왼쪽방향 회전
    if t == 0:
        for _ in range(k):
            # t가 0일 경우, 왼쪽 회전이므로 앞에 값이 뒤로 이동
            # pop을 수행하면 해당 인덱스값 삭제되고, 리스트 땡겨짐 이후 다시 추가함
            a[h-1].append(a[h-1].pop(0))
        else:
            # t가 1일 경우, 오른쪽 회전이므로 뒤에 값이 앞으로 이동
            for _ in range(k):
                a[h-1].insert(0, a[h-1].pop())

sum = 0
s = 0
e = n-1

for i in range(n):
    for j in range(s, e+1):
        sum += a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1

print(sum)