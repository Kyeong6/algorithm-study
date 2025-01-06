"""
숫자 A,B,C,D,E,F가 주어짐

Ax + By = C
Dx + Ey = F
x와 y값을 계산하는 프로그램을 작성하세요

x,y의 범위 : -10000 ~ 10000
"""

### My Solution

# a,b,c,d,e,f 입력
a, b, c, d, e, f = map(int, input().split())

for x in range(-999, 1000):
    for y in range(-999, 1000):
        if (a*x + b*y == c) and (d*x + e*y == f):
            print(x, y)
            break
            

