# 인접행렬: DFS
def solution(n, computers):
    
    def dfs(v):
        visited[v] = True
        
        # 인접노드 확인
        for adj in range(n):
            if not visited[adj] and computers[v][adj]:
                dfs(adj)
    
    cnt = 0
    visited = [False] * n
    
    for idx in range(n):
        if not visited[idx]:
            dfs(idx)
            cnt += 1
            
    return cnt