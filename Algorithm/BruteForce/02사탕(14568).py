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

### My Solution

# 사탕 개수
n = int(input())

    
### Correct Answer
n = int(input())

# 경우의 수 
cnt = 0

# A에게 주기
for a in range(0, n+1): # 0 ~ 6개
    # B에게 주기
    for b in range(0, n+1): # 0 ~ 6개
        # C에게 주기
        for c in range(0, n+1): # 0 ~ 6개

            # 조건 작성
            if a + b + c == n:
                if a >= b+2:
                    if (a != 0) and (b != 0) and (c != 0):
                        if c % 2 == 0:
                            cnt += 1
print(cnt)

"""
a,b,c에 각각 숫자를 넣어가면서 조건을 수행하는 것에 대해 이해가 부족
완전탐색적으로 생각한다면 for문을 이용해서 (a,b,c)에 각각 넣을 수 있음을 생각해보자
"""