from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    return bfs(begin, target, words)

# 최소 변환 갯수: BFS
def bfs(begin, target, words):
    
    queue = deque()
    queue.append([begin, 0]) # 시작단어 + 단계 0 초기화
    
    while queue:
        now, step = queue.popleft()
        
        if now == target:
            return step
        
        # 단어를 모두 체크하면서, 해당 단어가 변경될 수 있는지 체크
        for word in words:
            cnt = 0
            for i in range(len(now)):
                if now[i] != word[i]:
                    cnt += 1
            
            if cnt == 1:
                queue.append([word, step+1])