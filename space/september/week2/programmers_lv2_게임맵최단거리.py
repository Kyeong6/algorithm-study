from collections import deque

def solution(maps):
    
    n, m = len(maps), len(maps[0])
    visited = [[False]*m for _ in range(n)]
    
    # 큐 초기화 및 시작점 설정
    queue = deque()
    queue.append((0,0))
    
    # 방향 설정
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    while queue:
        x, y = queue.popleft()
        # 방문 처리
        visited[x][y] = True
        
        # 인접 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # 행렬 범위 내에 존재
            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                # 방문 여부 확인
                if not visited[nx][ny]:
                    # 방문 처리
                    visited[nx][ny] = True
                    
                    queue.append((nx, ny))
                    # 거리값으로 치환
                    maps[nx][ny] = maps[x][y] + 1
    
    # 도착점에서의 거리값이 1일 경우 
    if maps[n-1][m-1] == 1:
        return -1
    else:
        return maps[n-1][m-1]
            
    
    