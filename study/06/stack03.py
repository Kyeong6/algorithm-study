"""
괄호 회전하기:
"()", "{}", "[]"는 모두 올바른 괄호 문자열
만약 A가 올바른 괄호 문자열이라면 "(A)", "{A}", "[A]"도 올바른 괄호 문자열
즉, "[]"가 올바른 괄호 문자열이므로, "([])"도 올바른 괄호 문자열
만약 A,B가 올바른 괄호 문자열이라면 AB도 올바른 괄호 문자열
즉, "{}"와 "([])"가 올바른 괄호 문자열이므로 "{}([])"도 올바른 괄호 문자열
대괄호, 중괄호, 소괄호로 이루어진 문자열 s가 매개변수로 주어질 경우, s를 왼쪽으로 
x (0<= x <= (s길이))칸 만큼 회전시켰을 때 s가 올바른 괄호 문자열이 되게하는 x의 개수 반환

제약조건:
1. s의 길이는 1 ~ 1000

입출력 예시
s | result
"[](){}" | 3
"}]()[{" | 2
"[)(]" | 0
"""

"""
분석:
- 열린 괄호, 닫힌 괄호가 존재하기 때문에 동일한 종류의 '가장 최근'의 괄호를 맞춰야 함
- 즉, 열린 괄호를 스택에 push하여 관리
"""

# 검증 진행: O(N)
def is_valid(s: str) -> bool:
    stack = [] # 열린 괄호 담을 스택
    pairs = {
    ')': '(',
    '}': '{',
    ']': '['
    }

    # 순회를 통한 확인
    for c in s:
        if c in "({[":
            stack.append(c)
        elif c in ")}]":
            """
            조건1: 스택이 빈 상태에서 닫힌 괄호가 나오면 즉시 False
            조건2: 스택 맨 위(stack[-1])에 있는 열린 괄호가 c와 짝이 맞지 않으면 False
            """
            if not stack or stack[-1] != pairs[c]:
                return False
            
            stack.pop()
    
    # stack 비어있으면 True, 비어있지않으면 False
    return not stack
        

# 문자열 회전 진행: O(N)
def rotate(s: str) -> str:
    return s[1:] + s[0]

# 최종 실행 코드
def solution(s: str) -> int:
    n = len(s)
    cnt = 0
    curr = s

    # 각 함수들 O(N), n번 반복하므로 최종 시간복잡도는 O(N^2)
    for _ in range(n):
        if is_valid(curr):
            cnt += 1
        curr = rotate(curr)
    
    return cnt

# s = "[](){}"
# s = "}]()[{"
s = "[)(]"
print(solution(s))