"""
괄호 짝 맞추기:
소괄호 '(', ')'로 구성된 문자열 s가 주어짐
이때 괄호의 짝이 맞는지 판별하는 solution() 함수 구현
열린 괄호는 자신과 가장 가까운 닫힌 괄호를 만나면 상쇄되며, 이때 반드시 열린 괄호가 닫힌 괄호보다 먼저 와야함
괄호를 없애는 과정을 반복했을 때, 남아있는 괄호가 없으면 짝이 맞다고 할 수 있음

제약조건:
1. s의 길이는 최대 10만, 빈 문자열인 경우 x
2. 괄호의 짝이 맞으면 True, 짝이 맞지 않으면 False 반환

입출력 예시
s | 반환값
(())() | True
((())() | False
"""

"""
분석:
- 닫힌 괄호가 가장 최근의 열린 괄호와 상쇄 -> '스택' 사용
"""

def soultion(string):
    
    stack = [] # 열린 괄호 담을 스택
    
    # 순회를 통한 문자열 확인: O(N)
    for c in string:
        if c == "(":
            stack.append(c) # O(1)
        elif c == ")":
            # stack에 데이터가 없다는건 모두 ')'만 존재한다는 것: 바로 False
            if not stack:
                return False
            else:
                # 최신 '(' 제거
                stack.pop() # O(1)
    if stack:
        return False
    else:
        return True