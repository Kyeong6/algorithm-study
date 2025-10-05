"""
메모이제이션 : Top-Down
- 한 번 계산한 결과를 메모리 공간에 메모
    - 같은 문제를 다시 호출하면 메모했던 결과 그대로 가져옴
    - 캐싱이라고도 함
"""

# 피보나치 수열(Top-Down)

# 한 번 계산된 결과를 메모이제이션하기 위한 리스트 초기화(DP 테이블)
d = [0] * 100

# 피보나치(Top-Down Dynamic Programming): O(N)
def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    # 이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    
    # 계산하지 않은 문제는 점화식에 따라 피보나치 결과 수행
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))


# 피보나치(Bottom-Up Dynamic Programming)
d = [0] * 100

d[1] = 1
d[2] = 2
n = 99

# 피보나치 함수 반복문으로 구현
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])

