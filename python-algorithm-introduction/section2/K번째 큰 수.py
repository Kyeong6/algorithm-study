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