# 재귀 함수를 이용한 이진 탐색
def binary_search_recursive(array, target, start, end):
    if start > end:
        return None
    
    # 중간점(인덱스)
    mid = (start+end) // 2

    # 타겟값이 중간점
    if array[mid] == target:
        return mid
    
    # 타겟값이 중간점보다 적은 경우
    elif array[mid] > target:
        return binary_search_recursive(array, target, start, mid-1)
    
    # 타겟값이 중간점보다 큰 경우
    else:
        return binary_search_recursive(array, target, mid+1, end)
    

# 반복문을 이용한 이진 탐색
def binary_search_loop(array, target, start, end):
    while start <= end:
        mid = (start+end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

    
# # 입력 받기
# n, target = list(map(int, input().split()))
# array = list(map(int, input().split()))

# result = binary_search_recursive(array, target, 0, n-1)

# if result == None:
#     print("원소 미존재")
# else:
#     print(result+1)


