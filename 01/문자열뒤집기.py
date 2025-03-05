"""
방식: 바뀌는 순간에 카운트 진행
시간복잡도: O(N)
    - 단일 반복문
"""

def convert_string(string):
    cnt_zero = 0
    cnt_one = 0

    # 첫 번째 숫자 기준으로 그룹 개수 초기화
    # 예를 들어, 0으로 시작했으면 0으로 유지하는데 별다른 조치가 필요없지만, 
    # 모두 1로 만들려면, 첫 번째 0부터 1로 뒤집어야 하기 때문에 cnt_one += 1
    if string[0] == "0":
        cnt_one += 1
    elif string[0] == "1":
        cnt_zero += 1
    
    # 문자열 순회하며 변환 발생 지점 찾기
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                cnt_one += 1
            if string[i+1] == "1":
                cnt_zero += 1
    
    # 최소한의 뒤집기 횟수 반환
    return min(cnt_one, cnt_zero)


test = "0001100"
print(convert_string(test))