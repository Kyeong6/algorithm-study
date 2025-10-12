def solution(s):
    
    # stack -> list로 활용
    stack = []
    
    for i in s:
        # 열린 괄호일 경우
        if i == "(":
            stack.append(i)
        # 닫힌 괄호일 경우
        else:
            # 닫힌 괄호만 존재
            if not stack:
                return False
            else:
                # stack에 열린 괄호 존재
                stack.pop()
    
    # stack에 요소 남을 경우(Ex: "((" )
    if stack:
        return False
    
    return True