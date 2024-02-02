# 뒤집은 소수

n = int(input())
a = map(int, input().split())

# 뒤집는 함수 
def reverse(x):
    res = 0
    while (x>0):
        t = x % 10
        res = res * 10 + t
        x = x // 10

    return res

# 소수 판별 함수
def isPrime(x):
    if x == 1:
        return False
    # 해당 숫자의 절반까지만 돌면 됨 : 16 = 2 x 8과 같이 절반은 무조건 존재
    for i in range(2, x//2+1):
        # 약수가 존재한다면
        if x % i == 0:
            return False
    else:
        return True

for x in a:
    reverseNum = reverse(x)
    if isPrime(reverseNum) == True:
        print(reverseNum, end=' ')
