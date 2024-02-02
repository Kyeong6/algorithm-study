# 소수

n = int(input())

# 배열 생성
ch = [0] * (n+1)

# 소수의 개수 
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0:
        cnt += 1
        # step : i의 배수
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)

