"""
DFS: 재귀

- graph: 그래프 정보 (ex. 인접 리스트)
- start_node: 탐색 시작 노드
- visited: 방문 여부를 기록하는 리스트/집합
"""
def dfs_recursive(graph, v, visited):
    # 1. 현재 노드 방문 처리
    visited[v] = True
    print(v, end=' ') # 또는 원하는 로직 수행
    
    # 2. 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs_recursive(graph, i, visited)

# 사용 예시
# visited = [False] * (노드 개수 + 1)
# dfs_recursive(graph, start_node, visited)

"""
DFS: 스택
재귀 호출의 깊이 제한을 피할 때 유용한 방식
deque를 스택처럼 활용하여 직접 탐색 경로를 관리

- graph: 그래프 정보 (ex. 인접 리스트)
- start_node: 탐색 시작 노드
- visited: 방문 여부를 기록하는 리스트/집합
"""
from collections import deque

def dfs_stack(graph, start, visited):
    # 1. 덱(스택) 초기화
    stack = deque([start])
    
    while stack:
        # 2. 스택에서 가장 위에 있는 노드 추출 (LIFO)
        v = stack.pop()
        
        # 3. 방문하지 않은 노드인 경우에만 처리
        if not visited[v]:
            visited[v] = True
            print(v, end=' ') # 또는 원하는 로직 수행
            
            # 4. 인접 노드들을 스택에 삽입
            # 재귀 DFS와 동일한 순서를 위해 reversed를 사용하기도 함
            for i in reversed(graph[v]):
                if not visited[i]:
                    stack.append(i)

# 사용 예시
# visited = [False] * (노드 개수 + 1)
# dfs_stack(graph, start_node, visited)

"""
BFS: 큐
최단 거리를 구할 때 주로 사용되는 방식
deque를 큐처럼 활용하여 시작점에서 가까운 노드부터 탐색

- graph: 그래프 정보 (ex. 인접 리스트)
- start_node: 탐색 시작 노드
- visited: 방문 여부를 기록하는 리스트/집합
"""
from collections import deque

def bfs_queue(graph, start, visited):
    # 1. 덱(큐) 초기화
    queue = deque([start])
    
    # 2. 시작 노드 방문 처리
    visited[start] = True
    
    while queue:
        # 3. 큐에서 가장 앞에 있는 노드 추출 (FIFO)
        v = queue.popleft()
        print(v, end=' ') # 또는 원하는 로직 수행
        
        # 4. 인접 노드들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

# 사용 예시
# visited = [False] * (노드 개수 + 1)
# bfs_queue(graph, start_node, visited)