"""
다수의 소수 판별
    - 특정한 수의 범위 안에 존재하는 모든 소수 칮는 경우
    - 에라토스테네스의 체 알고리즘

- 에라토스테네스의 체 알고리즘
    1. 2 ~ N까지의 모든 자연수 나열
    2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i 찾기
    3. 남은 수 중에서 i의 배수 모두 제거(i는 제거 x)
    4. 더 이상 반복할 수 없을 때 까지 2,3번 과정 반복
"""

import math

n = 1000 # 2 ~ 1,000
array = [True for i in range(n+1)]

# 이때 제곱근 이용(결국 대칭이므로 절반만 확인 가능): O(NloglogN)
for i in range(2, int(math.sqrt(n))+1):
    if array[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

# 모든 소수 출력 
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')