"""
My Solution
- tmp = 0으로 초기값 설정할 경우 논리적 오류 존재
- 만약 입력 배열 arr의 첫 번째 원소가 0이라면, 그 0은 tmp와 같다고 판단되어 무시될 수 있음
"""
def solution(arr):
    
    lst = []
    tmp = 0 # 초기값
    
    # 삽입
    for i in range(len(arr)):
        if tmp == arr[i]:
            continue
        else:
            lst.append(arr[i])
            tmp = arr[i]
    
    return lst


# 정답 코드 (Me): 위에서 초기값 오류 해결
def solution(arr):
    
    lst = [arr[0]]
    tmp = arr[0] # 초기값
    
    # 삽입
    for i in range(1, len(arr)):
        if tmp == arr[i]:
            continue
        else:
            lst.append(arr[i])
            tmp = arr[i]
    
    return lst

# 정답 코드(Another)
def solution(arr):
    lst = []
    for i in range(len(arr)):
        if i == 0:
            lst.append(arr[i])
        else:
            if arr[i] != arr[i-1]:
                lst.append(arr[i])
    return lst