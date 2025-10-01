"""
10진수를 2진수로 변환하기:
10진수를 decimal을 입력받아 2진수로 변환하고 이를 문자열로 반환하는 solution() 함수 구현

제약조건:
1. decimal은 1000만 이하의 양의 정수

입출력 예시
decimal | 반환값
10 | "1010"
27 | "11011"
12345 | "11000000111001"
"""

"""
분석:
- 10진수를 2진수로 변환하는 과정은 다음과 같음
    - 10진수를 2로 나누어서 몫을 stack에 저장
    - stack에 있는 값들을 순서대로 가져와서 문자열로 변형
"""

def soultion(number) -> int:
    
    stack = [] # 스택 정의
    result = []
    string = ""

    # 2진수를 얻기위한 몫/나머지 연산 진행
    while True:
        if number == 0:
            break

        elem = number % 2
        stack.append(elem)
        number = number // 2

    for i in range(len(stack)):
        result.append(stack[-1-i])
    
    for j in range(len(result)):
        string += str(result[j])
    
    return string
    
number = 12345
# print(soultion(number))

"""
코드 수정: Develop
"""
def developSoultion(number):
    stack = []
    while number > 0:
        remainder = number % 2
        stack.append(str(remainder))
        number //= 2
    """
    아래 주석을 실행했을 경우 새로운 문자열을 매번 새로 생성
    즉, 1+2+3 ... +n -> O(N^2)
    위의 몫/나머지 연산이 O(logN)이므로 아래 주석을 실행하면 최종적으로 O((logN)^2)
    """
    # while stack:
    #     string += stack.pop()

    """
    reversed는 O(N), 즉 최종 시간 복잡도 O(logN)
    세부 구현 설명: join은 한 번에 n만큼 버퍼 한번 할당 후 리스트 요소 복사
    즉, 문자열을 하나 계속 업데이트하는 방식보다는 .join 연산 사용
    """
    return ''.join(reversed(stack))

number = 10
print(developSoultion(number))