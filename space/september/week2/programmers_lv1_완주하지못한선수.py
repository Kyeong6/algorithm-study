"""
바로 푼 문제
- 리스트와 리스트 비교: Hash(Dict) 사용
- 제한 사항에서의 최대 100,000명이기 때문에 시간복잡도 고려 필요: 이중반복문으로 인한 O(N^2) 사용 x

Hash를 이용하여 O(N)으로 해결 가능: Value를 통한 Key 찾기
    - 참고로, Key를 이용한 Value 찾기는 O(1)

- 리스트 정렬을 이용해서 푼다면?
    - sort() 함수로 인한 O(NlogN) 소요
"""

from collections import defaultdict

def solution(participant, completion):
    
    # 딕셔너리 생성: defaultdict를 통한 자동 0 초기화
    cnt = defaultdict(int)
    
    # 리스트 -> 딕셔너리
    for p in participant:
        cnt[p] += 1
        
    # 참여자와 완주자 비교: O(1)
    for c in completion:
        if cnt[c]:
            cnt[c] -= 1
    
    found_key = None
    # 값 출력: O(N)
    for key, value in cnt.items():
        if value == 1:
            found_key = key
            
    return found_key

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]

print(solution(participant, completion))