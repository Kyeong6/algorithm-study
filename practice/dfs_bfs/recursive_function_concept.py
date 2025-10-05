# 팩토리얼 구현 

# 반복적
def factorial_interative(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result

# 재귀적
def factorial_recursive(n):
    # 재귀적으로 구현할 경우 무조건 조건문 필요
    if n <= 1: # n이 1이하인 경우 1 반환
        return 1
    return n * factorial_recursive(n-1)


# 최대공약수 계산(유클리드 호제법)
def gcd(a, b):
    if a % b == 0:
        return b
    else:
        return gcd(b, a % b)
    
# print(gcd(192, 162))

