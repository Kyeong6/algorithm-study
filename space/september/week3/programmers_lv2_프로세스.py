"""
인덱스 비교 과정에서의 큐 적재 값(우선순위, 원래 위치) 확인 필요
"""

from collections import deque

def solution(priorities, location):
    # 큐에 (우선순위, 원래 위치) 저장
    queue = deque([(p, i) for i, p in enumerate(priorities)])
    
    answer = 0  # 실행 순서

    while queue:
        
        # 큐 사용이유 : 적재/삭제 - O(1)
        elem_priority, elem_location = queue.popleft()

        # 큐에 남은 프로세스들의 우선순위 확인
        # any() : 하나라도 True라면 True(max 함수 대신 이용)
        if any(elem_priority < p[0] for p in queue):
            # 우선순위가 더 높은 프로세스가 있다면 다시 큐에 적재
            queue.append((elem_priority, elem_location))
        else:
            answer += 1
            # 인덱스 비교
            if elem_location == location:
                return answer