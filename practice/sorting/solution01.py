"""
두 배열의 원소 교체

두 개의 배열 A, B은 N개의 원소로 구성(자연수)
최대 K번의 바꿔치기 연산 수행 가능, 바꿔치기 연산이란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나 골라서 두 원소 서로 바꾸기
최종 목표는 배열 A의 모든 원소의 합이 최대가 되도록 하는 것

- 입력 조건
1. 첫 번째 줄에 N, K가 공백을 기준으로 구분되어 입력 (1 <= N <= 100,000, 0 <= K <= N)
2. 두 번째 줄에 배열 A의 원소들 공백 기준으로 입력
3. 세 번째 줄에 배열 B의 원소들 공백 기준으로 입력

- 출력 조건
최대한 K번의 바꿔치기 연산 수행하여 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력

- 주의사항
     - 두 배열의 원소가 최대 100,000개까지 입력될 수 있으므로, 최악의 경우 O(NlogN) 보장하는 알고리즘 사용
"""

def change_list(a, b, k):
    
    # 배열 A 오름차순 정렬
    a.sort()
    # 배열 B 내림차순 정렬
    b.sort(reverse=True)

    # K번째 인덱스까지 스와핑 진행
    for i in range(k):
        if a[i] < b[i]:
            a[i], b[i] = b[i], a[i]
        else:
            break

    return sum(a)



# N, K 입력
n, k = map(int, input().split())

# 배열 정의
a = []
b = []

a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(change_list(a,b,k))
    