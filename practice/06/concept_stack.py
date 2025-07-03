"""
스택 활용:
- 최근에 삽입한 데이터를 대상으로 연산 수행할 경우
"""

stack = [] # 스택 리스트 초기화
max_size = 10 # 스택 최대 크기

def isFull(stack):
    return len(stack) == max_size

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    # 스택에 데이터 추가
    if isFull(stack):
        return
    else:
        return stack.append(item)

def pop(stack):
    if isEmpty(stack):
        return
    else:
        return stack.pop()
