# 점수 계산

# 문제 개수
n = int(input())

# OX 확인
a = list(map(int, input().split()))

sum = 0
cnt = 0

for i in range(len(a)):
    if a[i] == 1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0
print(sum)