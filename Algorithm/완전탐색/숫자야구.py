"""
A는 3자리 숫자로 된 정답을 하나 정함
B는 3자리 숫자를 제시해서 A가 생각하고 있는 정답을 맞히려고 함

B가 말한 숫자가 정답에 포함되어 있다면 1 Ball
B가 말한 숫자가 정답에 포함되어 있고, 자리 도 동일하다면 1 Strike

다른 숫자로 이루어진 세자리 수
Strike와 Ball의 결과를 보고, 가능한 숫자를 계산하는 프로그램 작성
"""

# 횟수 설정
n = int(input())

hint = [list(map(int, input().split())) for _ in range(4)]
answer = 0

# 100 ~ 999
for a in range(1, 10): # 100의 자리수
    for b in range(10): # 10의 자리수
        for c in range(10): # 1의 자리수
            
            # 다른 숫자로 이루어진 세자리 수 조건
            if (a == b or b == c or c == a):
                continue

            cnt = 0
                
            # 숫자가 정해졌다면 
            for arr in hint:
                number = hint[0]
                ball = hint[1]
                strike = hint[2]

                # a,b,c 라는 숫자를 number하고 비교
                # 자리수를 나눠서 stirke, ball을 측정하는 코드부분

                ball_count = 0
                strike_count = 0

                if ball == ball_count and strike == strike_count:
                    cnt += 1
                
            if cnt == n:
                answer += 1

print(answer)