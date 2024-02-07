# 격자판 최대합 

# 각 행의 합, 각 열의 합, 두 대각선의 합 중 가장 큰 합 출력
# 격자판 : 2차원 리스트

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

# 최대값 변수 초기화
largest = 0

for i in range(n):
    # 행/열의 합
    sum1 = sum2 = 0 
    for j in range(n):
        sum1 += a[i][j]
        sum2 += a[j][i]
    if sum1 > largest:
        largest = sum1
    if sum2 > largest:
        largest = sum2

# 대각선의 합
sum1 = sum2 = 0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1] # 예시를 들면 이해 가능
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2

print(largest)




