"""
- 수기로 작성한 로직은 맞았지만, 구현 과정에서 어려움을 겪은 문제
- Dict를 생성할 때 최종적으로 반환해야할 노래의 인덱스도 같이 포함 필요
- Dict로 시작했지만, 여러 배열을 이용해서 풀 수 있음을 확인한 문제
"""
from collections import defaultdict

def solution(genres, plays):
    
    # Dict 생성
    g_dict = defaultdict(list)
    for i in range(len(genres)):
        g_dict[genres[i]].append([i, plays[i]])
        
    # 장르별 재생횟수의 합 구한 후 오름차순 정렬
    h = [] # 정렬을 위한 새로운 배열 생성
    for key,value in g_dict.items():
        tmp = 0
        for _,v in value:
            tmp += v
        h.append([tmp,key])
    h.sort()
    
    # 장르별 재생횟수가 많은 순으로 결과값 추가
    result = []
    
    while h:
        key = h.pop()[1] # key 값 추출
        tmp = g_dict[key]
        tmp.sort(key=lambda x:x[1], reverse=True) # value(재생횟수) 기준 정렬
        
        # 장르에 속한 곡이 하나라면, 하나의 곡만 선택
        if len(tmp) == 1:
            result.append(g_dict[key][0][0])
        # 장르에 속한 곡 두 개 이상
        else:
            tmp = tmp[:2]
            for i in tmp:
                result.append(i[0])
                
    return result
            

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

print(solution(genres, plays))