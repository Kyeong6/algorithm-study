"""
Q. 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
Test Case: 10
Output: 3628800
"""
def factorial(number):

    # 탈출 조건
    if number == 1:
        return 1

    return number * factorial(number - 1)

number = 10
print(factorial(number))


"""
방식: 재귀함수 이용
"""

