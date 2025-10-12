"""
- Hash(Dict)를 이용하여 문제를 풀어야겠다고 판단까지 하였으나, '경우의 수'를 위한 수식 판단 x
    - 종류 : Key
- Key Point: A의 종류가 N개, B의 종류가 M개 일 때 가능한 모든 경우의 수는 (N+1)(M+1)
    - N, M에 각각 +1을 해주는 이유는 A를 사용하지 않는 경우, B를 사용하지 않는 경우를 포함하기 위함
    - 문제에서 최소 1개 이상의 의상을 입어야 한다고 제시
"""
from collections import defaultdict

def solution(clothes):
    
    # Dict 생성
    c_dict = defaultdict(int)
    for i in range(len(clothes)):
        c_dict[clothes[i][1]] += 1
        
    # 경우의 수: 2개의 종류 - (N+1)(M+1)-1 
    # -1 같은 경우 모두 사용하지 않은 경우를 제외
    result = 1
    for _,v in c_dict.items():
        result *= v+1 # Dict에서 Value끼리 곱할 경우 사용하는 로직  
        
    return result-1
