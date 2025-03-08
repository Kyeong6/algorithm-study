"""
Q. Merge Sort 구현
Test Case: [4, 6, 2, 9, 1]

방식: 분할정복(divide & conquer)을 이용한 merge sort 구현
    - MergeSort(0, N) = Merge(MergeSort(0, N/2) + MergeSort(N/2, N))
시간복잡도: O(NlonN)
    - 분할정복
"""
def merge(array1, array2):
    result = []
    array1_index = 0
    array2_index = 0
    while array1_index < len(array1) and array2_index < len(array2):
        if array1[array1_index] < array2[array2_index]:
            result.append(array1[array1_index])
            array1_index += 1
        else:
            result.append(array2[array2_index])
            array2_index += 1

    if array1_index == len(array1):
        while array2_index < len(array2):
            result.append(array2[array2_index])
            array2_index += 1

    if array2_index == len(array2):
        while array1_index < len(array1):
            result.append(array1[array1_index])
            array1_index += 1

    return result


def merge_sort(array):
    if len(array) <= 1:
        return array
    
    mid = len(array) // 2
    left_array = merge_sort(array[:mid])
    right_array = merge_sort(array[mid:])

    return merge(merge_sort(left_array), merge_sort(right_array))


array = [1, 2, 3, 5, 4, 6, 7, 8]
print(merge_sort(array))