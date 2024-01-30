# k번째 큰 수

# 조합 사용을 위한 라이브러리
from itertools import combinations as cb

# n,k 입력
n, k = map(int, input().split())
# elem 입력
elem = list(map(int, input().split()))

answer = list()

for i,j,m in cb(elem, 3):
    answer.append(i+j+m)

answer.sort(reverse=True)

print(answer[k-1])


# --------------------------------------

# 중복을 제거해줘야 한다.
# -> 합의 요소 중 K번째 이므로 중복이 있을 경우 답이 틀릴 경우가 존재

# 조합 사용을 위한 라이브러리
from itertools import combinations as cb

n, k = map(int, input().split())
elem = list(map(int, input().split()))
# 중복 제거하는 자료구조인 집합 사용
answer = set()

for i,j,m in cb(elem, 3):
    answer.add(i+j+m)

answer = list(answer)
answer.sort(reverse=True)

print(answer[k-1])


# --------------------------------------

# 다른 풀이

# 조합을 사용하지 않고, 3중 for문 사용

from itertools import combinations as cb

n, k = map(int, input().split())
elem = list(map(int, input().split()))

answer = set()

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            answer.add(answer[i]+answer[j]+answer[m])

answer = list(answer)
answer.sort(reverse=True)
print(answer[k-1])