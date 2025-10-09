"""
My Solution
"""
import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end, maps):

    answer = 0

    # 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    # 행렬 확인
    row, col = len(maps), len(maps[0])

    # 2차원 배열 생성
    check = [[0] * col for _ in range(row)]

    # 출발/도착 좌표 확인
    for i in range(row):
        for j in range(col):
            if maps[i][j] == start:
                start = [i, j]
            elif maps[i][j] == end:
                end = [i, j]

    # 출발지 좌표 설정
    x, y = start[0], start[1]

    # 큐 초기화
    queue = deque()
    queue.append([x, y, 0])

    # 큐가 비워질 때까지 수행
    while queue:
        x, y, res = queue.popleft()

        # 도착지 좌표 반환
        if x == end[0] and y == end[1]:
            return res

        # 네 방향 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < row and 0 <= ny < col:
                if check[nx][ny] == 0 and maps[nx][ny] != "X":
                    check[nx][ny] = 1
                    queue.append([nx, ny, res+1])

    return -1



def solution(maps):

    # S -> L
    to_lever = bfs("S", "L", maps)

    # L -> E
    to_end = bfs("L", "E", maps)

    if to_lever != -1 and to_end != -1:
        return to_lever + to_end

    return -1


"""
Another Solution
- 레버와 도착점 좌표를 미리 찾아둘 필요 없음
"""
from collections import deque

def solution(maps):
    answer = 0
    direction = [[0,1],[0,-1],[1,0],[-1,0]]
    n,m = len(maps),len(maps[0])

    # 출발 지점
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 'S':
                sx,sy = i,j
    
    # 레버 찾기
    def bfs(x,y,end):
        q = deque()
        q.append([x,y])

        visited = [[-1]*m for _ in range(n)]
        visited[x][y] = 0

        while q:
            x,y = q.popleft()
            if maps[x][y] == end:
                return [visited[x][y],x,y]
            for dir in direction:
                nx = x + dir[0]
                ny = y + dir[1]
                if 0 <= nx < n and 0 <= ny < m:
                    if visited[nx][ny] == -1:
                        if maps[nx][ny] != 'X':
                            q.append([nx,ny])
                            visited[nx][ny] = visited[x][y] + 1
        return None
    
    cnt = bfs(sx,sy,'L')

    if cnt == None:
        return -1
    
    answer += cnt[0]

    cnt = bfs(cnt[1],cnt[2],'E')
    
    if cnt == None:
        return -1
    
    answer += cnt[0]
    
    return answer
