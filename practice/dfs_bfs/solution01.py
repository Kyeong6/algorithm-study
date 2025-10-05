"""
음료수 얼려 먹기

- 입력 조건
1. 첫 번째 줄에 얼음 틀의 세로 길이 N과 가로 길이 M이 주어짐(1 <= N, M <= 1000)
2. 두 번째 줄부터 N+1번째 줄까지 얼음 틀의 형태가 주어짐
3. 이때 구멍이 뚫려있는 부분은 0, 그렇지 않은 부분은 1

- 출력 조건
한 번에 만들 수 있는 아이스크림의 개수 출력
"""

# DFS 활용
def dfs(x, y):
    # 주어진 인덱스 범위에 벗어나는 경우 즉시 종료: DFS의 기저 사례(Base Case)
    if x <= -1 or x >= n or y <= -1 or y >= m:
        return False
    
    # 현재 노드를 아직 방문 x
    # 조건: 해당 좌표의 값이 0일 경우
    if graph[x][y] == 0:
        # 방문 처리: 무한루프 방지
        graph[x][y] = 1
        # 상,하,좌,우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

n, m = map(int, input().split())

# 2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)
