# 자릿수의 합

n = int(input())
a = list(map(int, input().split()))

# 최댓값을 찾기 위한 max 변수 값 설정
max = 0

def digit_sum(x):
    # 자릿수를 더할 때 사용할 합할 값
    sum = 0
    # x>0인 이유는 마지막 자릿수 과정이 끝나면 몫인 x가 0이 되므로 break
    while (x>0):
        sum += x%10
        x = x//10

    return sum

# 리스트 요소의 값을 digit_sum()의 인자로 넘겨 자릿수 합 구하기
for x in a:
    total = digit_sum(x)
    # 자릿수의 합 중 최댓값 찾기
    if total > max:
        # for문 안에서 max 값 유지 : x의 값이 바껴도 전에 해당하는 값에 해당하는 max 값 유지되므로 갱신 가능
        max = total
        # 입력받은 수를 출력
        res = x

print(res)

# --------------------------

# Another Soultion
# 몫과 나머지 방식이 아닌 string 처리

def digit_sum(x):
    sum = 0
    for i in str(x):
        sum += int(i)

    return sum