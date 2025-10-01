"""
배열 정렬하기:
정수 배열을 오름차순 정렬해서 반환하는 solution() 함수 완성

제약조건:
1. 정수 배열의 길이는 2 이상 10^5 이하
-> 데이터의 개수가 최대 10^5이므로 제한 시간이 3초라면 O(N^2) 알고리즘 사용 불가
2. 제한시간 3초
"""

import time

# sort(): O(NlogN)
def solution(arr):
    arr.sort()
    return arr

# sort() 메서드 사용하지 않고 이중반복문을 사용했다면?: O(N^2)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[i] > arr[j+1]:
                arr[j], arr[i] = arr[j+1], arr[i]
    
    return arr

# 시간 측정
def measure_time(func, arr):
    start_time = time.time()
    result = func(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time

    return elapsed_time, result

arr = list(range(10000))

# O(N^2): 
bubble_time, bubble_result = measure_time(bubble_sort, arr)
print(f"O(N^2): {bubble_time}")

# O(NlogN): 
sort_time, sort_result = measure_time(solution, arr)
print(f"O(NlogN): {sort_time}")