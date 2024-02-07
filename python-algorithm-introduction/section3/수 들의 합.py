# 수들의 합

# n,m 입력
n,m = map(int, input().split())

# 수열 생성
a = list(map(int, input().split()))

# 진행을 위한 인덱스 설정
lt = 0 
rt = 1

# 연속부분의 합
tot = a[0]

# 경우의 수
cnt = 0

while True:
    if tot < m:
        if rt < n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt += 1
    else:
        tot -= a[lt]
        lt += 1

print(cnt)