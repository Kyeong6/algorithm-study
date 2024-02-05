# 회문 문자열 검사

# 횟수 입력
n = int(input())

for i in range(n):
    a = input()
    # 대소문자 구별x
    a = list(a.lower())
    # 회문 판별을 위해 list 
    rev = list(reversed(a))
    if a == rev:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))


# -----------------------------------

# Another Soultion-1

# reverse() 사용 x, 정석풀이
for i in range(n):
    s = input()
    s = s.lower()
    size = len(s)
    # // 사용하여 홀수일 경우 가운데 무시 가능
    for j in range(size//2):
        if s[j] != s[-1-j]:
            print("#{} NO".format(i+1))
            break
    else:
        print("#{} YES".format(i+1))


# -----------------------------------

# 슬라이싱 사용
for i in range(n):
    s = input()
    s = s.upper()
    if s == s[::-1]:
        print("#{} YES".format(i+1))
    else:
        print("#{} NO".format(i+1))