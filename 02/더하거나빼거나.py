"""
Q. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
Test Case:
numbers = [1, 1, 1, 1, 1]
target_number = 3
numbers = [4,1,2,1]
target_number = 4

방식: 두 가지 방식 사용
    - DFS(재귀) 이용
    - 최적화를 위한 메모이제이션(중복 x)
시간복잡도:
    - DFS: O(2^N)
    - 메모이제이션: O(N*S) -> S는 숫자의 합의 최대 크기
"""
def basic_find_target_number(target, numbers):
    # 모든 숫자를 다 사용했을 때, 총합이 target과 같으면 1 반환
    def dfs(index, total):
        if index == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        # 현재 숫자를 더하는 경우와 빼는 경우의 모든 경우 탐색
        return dfs(index + 1, total + numbers[index]) + dfs(index + 1, total - numbers[index])
    
    # 초기값 설정
    return dfs(0,0)

def improve_find_target_number(target , numbers):
    # (index, total) 값 저장
    memo = {}

    def dfs(index, total):
        # 이미 계산된 값 존재하는지 확인
        if (index, total) in memo:
            return memo[(index, total)]
        
        # 모든 숫자를 사용했을 때, 목표값과 같으면 1 반환
        if index == len(numbers):
            if total == target:
                return 1
            else:
                return 0
        
        # 현재 숫자를 더하는 경우와 빼는 경우 탐색
        count = dfs(index + 1, total + numbers[index]) + dfs(index + 1, total - numbers[index])

        # 결과 저장
        memo[(index, total)] = count
        return count
    
    # 초기값 설정
    return dfs(0,0)

first_test_case = [1, 1, 1, 1, 1]
first_target = 3
second_test_case = [4,1,2,1]  
second_target = 4
print(basic_find_target_number(first_target, first_test_case))
print(basic_find_target_number(second_target, second_test_case))
print(improve_find_target_number(first_target, first_test_case))
print(improve_find_target_number(second_target, second_test_case))