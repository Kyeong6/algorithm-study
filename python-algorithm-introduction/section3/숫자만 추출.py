# 숫자만 추출

# 문자 입력
s = input()
res = 0

# 숫자 추출, 자연수화(0은 자연스럽게 사라짐)
for x in s:
    if x.isdigit(): # 0~9는 isdecimal() 사용 가능
        res=res*10+int(x)
print(res)

# 약수 개수
cnt = 0
for i in range(1, res+1):
    if res % i == 0:
        cnt += 1
print(cnt)
