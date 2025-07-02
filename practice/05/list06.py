"""
실패율:
실패율 정의는 다음과 같다.
스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어의 수
전체 스테이지 개수가 N, 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열
stages가 주어질 때 실패율이 높은 스테이지부터 내림차순으로 스테이지의 번호가 담겨있는 배열 반환

제약조건:
1. 스테이지 개수 N: 1 ~ 500
2. stage 길이: 1 ~ 200,000
3. stages에는 1 ~ N+1 자연수
    - 각 자연수는 사용자가 현재 도전 중인 스테이지 번호
    - 단, N+1은 마지막 스테이지, 즉 N까지 클리어한 사용자
4. 만약 실패율이 같은 스테이지가 있다면 작은 번호의 스테이지가 먼저 오면 됨
5. 스테이지에 도달할 유저가 없는 경우 해당 스테이지의 실패율은 0으로 정의

분석:
- stages 길이가 1 ~ 200,000이므로 O(NlogN) 사용
- N: 스테이지 개수, M: stages 길이
"""
def solution(n, stages):
    
    # 스테이지별 도전자 수 
    challenger = [0] * (n+2)
    for stage in stages:
        challenger[stage] += 1

    # 스테이지별 실패한 사용자 수 계산
    fails = {}
    total = len(stages)

    # 각 스테이지를 순회하여 실패율 계산: O(N+M)
    for i in range(1, n+1):
        if challenger[i] == 0: # 도전한 사람 x
            fails[i] = 0
        else:
            # 실패율
            fails[i] = challenger[i] / total
            # 다음 스테이지 실패율 구하기 위해 현재 스테이지 인원 빼기
            total -= challenger[i]

    # 내림차순 정렬: O(NlogN)
    result = sorted(fails, key=lambda x: fails[x], reverse=True)

    return result

n = 5
stages = [2,1,2,6,2,4,3,3]
print(solution(n, stages))