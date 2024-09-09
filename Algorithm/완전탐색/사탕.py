# 사탕

"""
친구 A,B,C에게 사탕을 나누어 주려고 한다.
조건:
1. 남는 사탕이 없어야 함
2. A는 B보다 2개 이상 많은 사탕 가져야 함
3. 셋 중 사탕을 하나도 못 받는 사람은 존재 x
4. C가 받는 사탕의 수는 짝수

분배가 가능한 경우의 수 출력하는 프로그램 작성
"""

# 사탕의 수 지정
candy = int(input())

# 경우의 수
cnt = 0

# A는 0 ~ 6개를 줄 수 있음
for a in range(0, candy+1):
    # B는 0 ~ 6개를 줄 수 있음
    for b in range(0, candy+1):
        # C는 0 ~ 6개를 줄 수 있음
        for c in range(0, candy+1):
            # 조건1
            if a + b + c == candy:
                # 조건2
                if a >= b+2:
                    # 조건3
                    if a != 0 and b != 0 and c != 0:
                        # 조건4
                        if c % 2 == 0:
                            cnt += 1

print(cnt)