"""
Q. Bubble Sort 구현
Test Case: [4, 6, 2, 9, 1]

방식: swap을 이용한 bubble sort 구현
시간복잡도: O(N^2)
    - 이중 반복문 사용
"""
def bubble_sort(array):
    n = len(array)
    for i in range(n-1):
        # 반복횟수 주의 필요(처음 구현했을 때 답은 맞았지만 의미없는 횟수까지 진행해버림)
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                # swap
                array[j], array[j+1] = array[j+1], array[j]
            # array[j] <= array[j+1]
            else:
                continue
    
    return array

input = [4, 6, 2, 9, 1]
print(bubble_sort(input))