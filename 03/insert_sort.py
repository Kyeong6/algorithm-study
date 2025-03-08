"""
Q. Insert Sort 구현
Test Case: [4, 6, 2, 9, 1]

방식: swap을 이용한 insert sort 구현
시간복잡도: O(N^2)
    - 이중 반복문 사용
    - 최선의 경우는 N이 걸림(이미 다 정렬되어있다면 혹은 부분적으로 정렬이 되어있다면 break 되기때문)
    - 앞의 bubble, select는 무조건 O(N^2)
"""
def insert_sort(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i):
            if array[i-j] < array[i-j-1]:
                array[i-j], array[i-j-1] = array[i-j-1], array[i-j]
            # 이미 정렬되어있으면 다음 반복문 이동
            else:
                break
        
    return array

input = [4, 6, 2, 9, 1]
print(insert_sort(input))