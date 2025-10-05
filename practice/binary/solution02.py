"""
정렬된 배열에서 특정 수의 개수 구하기

N개의 원소를 포함하고 있는 수열이 오름차순으로 정렬
수열에서 x가 등장하는 횟수 계산
예를 들어, {1,1,2,2,2,2,3}이 있을 때 x=2라면, 4 출력
단, 시간 복잡도 O(logN)으로 설계하지 않으면 시간 초과 판정 받음
    - 일반적인 선형탐색으로는 시간 초과 판정, 데이터 정렬되어 있기 때문에 이진 탐색 수행 필요

- 입력 조건
1. 첫째 줄에 N과 x가 정수 형태로 공백으로 구분되어 입력
2. 둘째 줄에 N개의 원소가 정수 형태로 공백으로 구분되어 입력

- 출력 조건
수열의 원소 중에서 값이 x인 원소의 개수 출력, 단 값이 x인 원소가 하나도 없다면 -1 출력
"""

from bisect import bisect_left, bisect_right

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)

    result = right_index - left_index
    
    if result != 0:
        return result
    else:
        return -1


# 입력
n, x = map(int, input().split())
array = list(map(int, input().split()))

print(count_by_range(array, x, x))