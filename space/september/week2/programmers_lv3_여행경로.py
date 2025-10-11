"""
DFS 방식까지 접근한 문제
- defaultdict 알게 됨
- DFS -> Stack : Stack은 LIFO이기 때문에 조건에서의 도착지 우선을 위해서는 reverse=True 진행 필요
"""

from collections import defaultdict

def solution(tickets):
    
    # key : 출발지, value : 목적지
    ticket_dict = defaultdict(list)
    
    # 목적지 기준 역순 정렬 : pop() 진행 시에 알파벳 순으로 나오도록 하기 위해
    tickets.sort(reverse=True)
    
    # 그래프 생성
    for start, end in tickets:
        ticket_dict[start].append(end)
        
    path = []
    stack = ["ICN"]
    
    # Stack
    while stack:
        current_airport = stack[-1]
        
        # 현재 공항에서 출발하는 티켓이 남아있을 때
        if current_airport in ticket_dict and ticket_dict[current_airport]:
            next_airport = ticket_dict[current_airport].pop()
            stack.append(next_airport)
        # 현재 공항이 막다른 길일 때
        else:
            path.append(stack.pop())
    
    # 경로 역순으로 뒤집어서 반환
    return path[::-1]