"""
- 앞기능이 배포되어야지 뒷기능이 배포하는 로직 구현 못함
- 잔여일 확인을 위해 while문을 이용한 빼기 과정을 진행했지만, 더 효율적인 방식 존재
"""
def solution(progresses, speeds):
    
    # 잔여일자 확인을 위한 배열 생성
    p = []
    for i in range(len(progresses)):
        res = 0
        res = 100 - progresses[i]
        p.append(res)
    
    # 잔여일 확인
    days = []
    for i in range(len(speeds)):
        
        speed = speeds[i]
        percent = p[i]

        # 같은 인덱스의 두 원소를 가져와서 뺼셈 시작
        cnt = 0  # 뺼셈 횟수
        while percent > 0:
            percent -= speed
            cnt += 1
        days.append(cnt)
    
    res = []
    # 잔여일 앞뒤비교 진행
    
"""
정답 코드
- zip() : 병렬로 묶어주는 함수(리스트와 같은 iterable 요소 활용)
    - 참고로 enumerate() 같은 경우는 인덱스를 얻을 때 활용
- (100 - p) / s는 남은 진도를 속도로 나눈 값
    - 남은 진도가 5%이고 속도가 4%라면 5/4 = 1.25가 나옵니다. 배포는 하루의 끝에 이루어지므로, 소수점은 올림하여 2일
- dyas_to_complete[0] : 다음 기능 의미
"""
import math
from collections import deque

def solution(progresses, speeds):

    result = []
    # 각 기능이 완성되기까지 필요한 일수를 계산하여 큐에 저장
    days_to_complete = deque()
    for p, s in zip(progresses, speeds):
        days = math.ceil((100 - p) / s)
        days_to_complete.append(days)

    # 큐를 순회하며 배포 그룹 찾기
    while days_to_complete:
        # 현재 배포 그룹의 기준이 될 기능의 배포일을 가져옴
        first_deploy_day = days_to_complete.popleft()
        cnt = 1

        # 기준일보다 먼저 완성되는 다음 기능들을 모두 함께 배포
        while days_to_complete and days_to_complete[0] <= first_deploy_day:
            days_to_complete.popleft()
            cnt += 1
            
        result.append(cnt)
    
    return result