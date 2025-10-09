"""
백준 1012번 - 유기농 배추

배추흰지렁이가 한 마라리라도 살고 있으면 이 지렁이는 인접한 다른 배추로 이동할 수 있어, 배추들 해충으로부터 보호받을 수 있음
한 배추의 상하좌우 네 방향에 다른 배추가 위치한 경우에 서로 인접해있는 것

0은 배추가 심어져 있지 않은 땅, 1은 배추가 심어져 있는 땅
1인 연결된 구역이라면 1마리의 배추흰지렁이가 필요

- 입력 조건
1. 첫째 줄에는 테스트 케이스의 개수 T가 주어짐
2. 둘째 줄에는 각각의 테스트 케이스에 대해 첫째 줄에는 배추를 심은 배추밭의 가로길이 M(1 <= M <= 50), 세로 길이 N(1 <= N <= 50)
그리고, 배추가 심어져 있는 위치의 개수 K(1 <= K <= 2500)이 주어짐
3. 다음 K줄에는 배추의 위치(O <= X <= M-1), Y(0 <= Y <= N-1)가 주어짐
"""

import sys
input = sys.stdin.readline

# 재귀함수 호출 깊이 100만으로 늘리기
sys.setrecursionlimit(10**6)

def dfs(x, y):
    # 종료 조건: 범위
    if x < 0 or x >= m or y < 0 or y >= n:
        return False
    
    if graph[x][y] == 1:
        # 방문 처리
        graph[x][y] = 0
        dfs(x, y+1) # 상
        dfs(x, y-1) # 하
        dfs(x-1, y) # 좌
        dfs(x+1, y) # 우
        return True
    
    return False


# 입력받기
tc = int(input()) # 테스트 케이스

for t in range(tc):
    m, n, k = map(int, input().split())
    worm = []
    for i in range(k):
        worm.append(list(map(int, input().split())))

    graph = [[0] * n for _ in range(m)]

    # worm 리스트의 각 좌표를 graph 배열에 1로 표시
    for coordinate in worm:
        x, y = coordinate[0], coordinate[1]
        graph[x][y] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if dfs(i,j):
                result += 1
    print(result)
    result = 0