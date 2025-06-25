"""
Q. 회문검사 진행
Test Case: addda
"""
def is_palindrome(string):
    n = len(string)
    for i in range(n):
        # 앞뒤 확인
        if string[i] != string[n-1-i]:
            return False
        
    return True

# 범위 줄여나가기: 앞뒤 확인했으면 필요없으니 나머지만 검사
def is_palindrome_recursion(string):

    if string[0] != string[-1]:
        return False
    
    # 한글자일 경우 무조건 회문
    if len(string) <= 1:
        return True

    # 문자열 자르기
    return is_palindrome_recursion(string[1:-1])

test_case = "addda"
print(is_palindrome(test_case))
print(is_palindrome_recursion(test_case))

"""
방식: 재귀함수 이용
"""