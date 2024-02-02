# 대표값

# 입력 받기
n = int(input())
a = list(map(int, input().split()))

# 점수의 평균
avg = round((sum(a) / len(a)))

# 정수형에서 가장 큰값 설정
min = 2147000000

for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < min:
        min = tmp
        score = x
        res = idx+1
    # 같은 거리가 나왔을 경우
    elif tmp == min:
        if x > score:
            score = x
            res = idx+1

print(avg, res)
    