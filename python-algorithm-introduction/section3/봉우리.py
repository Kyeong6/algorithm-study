# 봉우리

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 상하좌우 x,y로 표현(네 방향 탐색)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 가장자리 0으로 초기화
# 0번 행에 [0] n개만큼 생성
a.insert(0, [0]*n) 

# append는 마지막에 추가, 즉 insert 사용하지 않아도 됨
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

# 상하좌우 탐색
for i in range(1, n+1):
    for j in range(1, n+1):
        # all() : 모두 참일 경우 실행
        if all(a[i][j]>a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt += 1

print(cnt)
            

