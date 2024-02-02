# 정다면체

n, m = map(int, input().split())

# cnt 변수 설정
cnt = [0] * (n+m+1)
max = 0
    
for i in range(1, n+1):
    for j in range(1, m+1):
        # 해당하는 인덱스 횟수 추가
        cnt[i+j] += 1

# cnt의 최댓값 찾기
for i in range(n+m+1):
    if cnt[i] > max:
        max = cnt[i]

# 최댓값에 해당하는 인덱스 출력
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')