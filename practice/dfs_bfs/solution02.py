"""
미로 탈출

N x M 크기의 직사각형 형태의 미로, 장애물을 피해 탈출 필요
위치는 (1, 1)이며 미로의 출구는 (N, M)의 위치에 존재하며 한 번에 한 칸씩 이동
장애물 있는 부분은 0, 없는 부분은 1로 표시


- 입력 조건
1. 첫째 줄에 두 정수 N, M(4<=N, M<=200)이 주어짐
2. 다음 N개의 줄에는 각각 M개의 정수(0 혹은 1)로 미로의 정보가 주어짐
3. 각각의 수들은 공백 없이 입력을 제시, 또한 시작 칸과 마지막 칸은 항상 1

- 출력 조건
탈출하기 위해 움직여야 하는 최소 칸의 개수, 칸을 셀 때는 시작 칸과 마지막 칸을 모두 포함해서 계산
"""
from collections import deque

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        # 현재 위치에서 4가지 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우 무시
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 벽인 경우 무시
            if graph[nx][ny] == 0:
                continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]


# 행 / 열 입력
n, m = map(int, input().split())

graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 이동할 네 가지 방향 정의(상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 수행 결과
print(bfs(0,0))