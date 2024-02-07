# 두 리스트 합치기

# 첫 번째 리스트 수
n = int(input())
a = list(map(int, input().split()))

# 두 번째 리스트 수
m = int(input())
b = list(map(int, input().split()))

# 첫 번재 리스트와 두 번째 리스트 합치기
c = a+b

# Solution1 : 오름차순 정렬 sort() 사용
c.sort()

print(c)

# ------------------------

# 위의 풀이는 nlong의 시간복잡도를 갖음
# 이미 정렬되어 있는 두 리스트를 합치는 것이므로 n번만에 수행할 수 있음

# Solution

# 첫 번째 리스트 수
n = int(input())
a = list(map(int, input().split()))

# 두 번째 리스트 수
m = int(input())
b = list(map(int, input().split()))

p1 = p2 = 0
c = list()

# 두 리스트 비교
while (p1 < n) and (p2 < m):
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1

# 남은 자료 확인
if p1 < n:
    # a 리스트 중간 부분이 b리스트의 마지막 부분보다 크므로 나머지 부분을 슬라이싱을 이용하여 붙이기
    c = c + a[p1:]
if p2 < m:
    c = c + b[p2:]

for x in c:
    print(x, end=' ')



