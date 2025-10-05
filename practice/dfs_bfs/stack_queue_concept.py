# Stack
def execute_stack():
    stack = []

    stack.append(5)
    stack.append(2)
    stack.append(3)
    stack.append(7)
    stack.pop()
    stack.append(1)
    stack.pop()

    return stack

final_stack = execute_stack()

# # 최상단부터 호출
# print(final_stack[::-1])

# # 최하단부터 호출
# print(final_stack)

# Queue
from collections import deque

def execute_queue():

    # Queue 정의
    queue = deque()

    queue.append(5)
    queue.append(2)
    queue.append(3)
    queue.append(7)
    queue.popleft()
    queue.append(1)
    queue.popleft()

    return queue

final_queue = execute_queue()

# 먼저 들어온 순 출력
print(final_queue)

# 역순
final_queue.reverse()
print(final_queue)