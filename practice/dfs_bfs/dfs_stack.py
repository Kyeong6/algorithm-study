from collections import deque

# DFS 메서드 정의 (스택 기반)
def dfs_stack(graph, start, visited):
    # deque를 스택처럼 사용
    stack = deque([start])

    while stack:
        # 스택에서 하나의 원소 추출(LIFO)
        v = stack.pop()
        
        # 현재 노드가 방문되지 않았을 경우에만 처리
        if not visited[v]:
            visited[v] = True
            print(v, end=' ')

            # 인접 노드들을 스택에 삽입: 역순으로 삽입하면 재귀 DFS와 동일한 탐색 순서가 됨
            for i in reversed(graph[v]): 
                if not visited[i]:
                    stack.append(i)

# 각 노드가 연결된 정보 표현: 1번 노드부터 시작
graph = [
    [], # graph 문제 출제시 노드 번호가 1번부터 시작하니까 index 0은 비우기
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]

# 각 노드가 방문된 정보 표현
visited = [False] * 9

# 스택 기반 DFS 함수 호출
dfs_stack(graph, 1, visited)
print()