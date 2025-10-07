"""
- 특정한 노드에서 출발하여 다른 모든 노드로 가는 최단 경로 계산
- 다익스트라 최단 경로 알고리즘은 음의 간선이 없을 때 정상적으로 동작
    - 현실 세계의 도로(간선)은 음의 간선으로 표현되지 않음
- 다익스트라 최단 경로 알고리즘은 그리디 알고리즘으로 분류
    - 매 상황에서 가장 비용이 적은 노드를 선택해 임의의 과정 분류

- 동작 과정
    1. 출발 노드 설정
    2. 최다 거리 테이블 초기화
    3. 방문하지 않은 노드 중에서 최단 거리가 가장 짧은 노드 선택
    4. 해당 노드를 거쳐 다른 노드로 가는 비용 계산하여 최단 거리 테이블 갱신
    5. 위 과정에서 3,4번 반복

- 한 번 처리된 노드의 최단 거리는 고정되어 더 이상 바뀌지 않음
    - 한 단계당 하나의 노드에 대한 최단 거리를 확실히 찾는 것으로 이해

- 총 O(V)번에 걸쳐서 최단 거리가 가장 짧은 노드를 매번 선형 탐색
    - 전체 시간 복잡도 : O(V^2) - V는 노드의 개수
- 일반적으로 최단 경로 문제에서 전체 노드의 개수가 5,000개 이하라면 사용
"""

import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값

# 노드의 개수, 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드 번호 입력받기
start = int(input())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 방문 여부 체크하는 목적의 리스트 만들기
visited = [False] * (n+1)

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

# 모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미
    graph[a].append((b,c))

# 방문하지 않은 노드 중에서 가장 최단 거리가 짧은 노드의 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 가장 최단 거리가 짧은 노드(인덱스)
    for i in range(1, n+1):
        if distance[i] < min_value and not visited[i]:
            min_value = distance[i]
            index += 1
    return index

def dijkstra(start):
    # 시작 노드에 대해서 초기화
    distance[start] = 0
    visited[start] = True
    for j in graph[start]:
        distance[j[0]] = j[1]
    # 시작 노드를 제외한 전체 n-1개의 노드에 대해 반복
    for i in range(n-1):
        # 현재 최단 거리가 가장 짧은 노드를 꺼내서, 방문 처리
        now = get_smallest_node()
        visited[now] = True
        # 현재 노드와 연결된 다른 노드를 확인
        for j in graph[now]:
            cost = distance[now] + j[1]
            # 현재 노드를 거쳐서 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[j[0]]:
                distance[j[0]] = cost

# 다익스트라 알고리즘 수행
dijkstra(start)

# 모든 노드로 가기 위한 최단 거리 출력
for i in range(1, n+1):
    # 도달할 수 없는 경우, 무한이라고 출력
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])