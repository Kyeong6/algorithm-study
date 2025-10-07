"""
소수 판별

- 소수란?
    - 1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어떨어지지 않는 자연수
"""

# 기본: O(X)
def is_prime_number(x):
    # 2부터 (x-1)까지의 모든 수 확인
    for i in range(2, x):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))

# 개선: O(N^1/2)
import math

def is_prime_number_advance(x):
    # 2부터 x의 제곱근까지의 모든 수 확인
    for i in range(2, int(math.sqrt(x)) + 1):
        # x가 해당 수로 나누어떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number_advance(7))