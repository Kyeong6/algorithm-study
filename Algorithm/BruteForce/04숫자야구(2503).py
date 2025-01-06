"""
A는 3자리 숫자로 된 정답을 하나 정함
B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 함

B가 말한 숫자가 정답에 포함되어 있다면 1 Ball
B가 말한 숫자가 정답에 포함되어 있고, 자리도 동일하다면 1 Strike

다른 숫자로 이루어진 세자리 수
Strike와 Ball의 결과를 보고, 가능한 숫자를 계산하는 프로그램 작성
"""

### Correct Answer
import sys
# 순열: 순서를 고려해 나열한 경우의 수 (A,B) != (B,A)
# 9P3 == 504(경우의 수)
from itertools import permutations

input = sys.stdin.readline

# 횟수
n = int(input())

# 입력받은 숫자, 스트라이크, 볼 저장
hint = [list(map(int, input().split())) for _ in range(n)]

# 답 개수 변수 
cnt = 0

# 1 ~ 9 중 서로 다른 3개를 골라 세자리 수 만들기: 모든 세자리 경우의 수를 저장하는 방식 -> 완전탐색
# 3중 for문 이용 가능: 조건 필요
nums = list(permutations(range(1, 10), 3))

# 답 확인
for num in nums:
    # 정답 가능 나타내는 플래그
    valid = True

    for arr in hint:
        hint_num = list(map(int, str(arr[0])))
        hint_strikes, hint_balls = arr[1], arr[2]

        # 스트라이크, 볼 수 초기화
        strikes = balls = 0

        # 계산
        for i in range(3):
            # 같은 자리 같은 숫자: strike
            if num[i] == hint_num[i]:
                strikes += 1
            # 다른 자리 같은 숫자: ball
            elif num[i] in hint_num:
                balls += 1
        
        # 유효한지 확인
        if hint_strikes != strikes or hint_balls != balls:
            valid = False
            break

    # 모든 조건 만족하면 경우의 수 증가
    if valid:
        cnt += 1

print(cnt)

    


