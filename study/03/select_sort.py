"""
Q. Select Sort 구현
Test Case: [4, 6, 2, 9, 1]

방식: swap을 이용한 select sort 구현
시간복잡도: O(N^2)
    - 이중 반복문 사용
"""
def select_sort(array):
    n = len(array)
    # 범위 사용
    for i in range(n-1):
        min_index = i
        # 비교 사용
        for j in range(n-i):
            if array[i+j] < array[min_index]:
                min_index = i + j
        array[i], array[min_index] = array[min_index], array[i]

    return array

input = [4, 6, 2, 9, 1]
print(select_sort(input))