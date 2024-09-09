"""
숫자 A,B,C,D,E,F가 주어짐

Ax + By = C
Dx + Ey = F
x와 y값을 계산하는 프로그램을 작성하세요

x,y의 범위 : -10000 ~ 10000
"""

# 수 입력
a,b,c,d,e,f = map(int, input().split())

for x in range(-10000, 10001):
    for y in range(-10000, 10000):
        # 두 개의 조건문을 하나의 조건문으로 생각할 수 있지만 이중 조건문으로 나눌 수 있음
        if a*x + b*y == c:
            if d*x + e*y == f:
                print(x, y)
                break