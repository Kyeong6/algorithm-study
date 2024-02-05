# 카드 역배치

# 숫자 리스트 생성
a = list()

for i in range(1,21):
    a.append(i)

# 범위 변환
for _ in range(10):
    f,s = map(int, input().split())
    ext = a[f-1:s]
    ext = reversed(ext)
    a[f-1:s] = ext

print(*a)


# --------------
# Another solution(정석)
a = list(range(21))
for _ in range(10):
    f,s = map(int, input().split())
    for i in range((s-f+1)//2):
        a[f+i], a[s-i] = a[s-i], a[f+i]

a.pop(0) # 0번 인덱스 제거
for x in a:
    print(x, end=' ')

