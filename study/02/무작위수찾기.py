"""
Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 
2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.
Test Case: [0, 3, 5, 6, 1, 2, 4]
"""
def is_existing_number(target, array):
    array = sorted(array)
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if array[cur_guess] == target:
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1

        cur_guess = (cur_min + cur_max) // 2
    
    return False

target = 2
array = [0, 3, 5, 6, 1, 2, 4]
print(is_existing_number(target, array))

"""
방식: 현재 문제는 배열이 존재할 때 탐색을 하는 문제, 이때 가장 효율적인 방식은 '이진탐색'
    - 이진탐색의 전제조건은 '정렬'
시간복잡도: O(NlogN)
    - 정렬: O(NlonN)
    - 이진 탐색: O(logN)
"""