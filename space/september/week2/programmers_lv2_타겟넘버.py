# BFS
def solution(numbers, target):
    # 진행을 위한 초기값
    leaves = [0]
    cnt = 0
    
    # 완전 탐색: 2^n
    for num in numbers:
        temp = []
        for elem in leaves:
            temp.append(elem + num)
            temp.append(elem - num)
        leaves = temp
    
    # 타겟과의 매칭 확인
    for elem in leaves:
        if target == elem:
            cnt += 1
            
    return cnt