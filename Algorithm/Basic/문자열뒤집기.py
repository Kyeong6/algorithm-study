"""
방식: 뒤집는 수 선정은 0과1의 개수 중 더 적은 것을 뒤집기
    - 테스트 케이스를 토대로 개수가 동일하면 어떤 수를 뒤집어도 같음
시간복잡도: O(N)
    - 단일 반복문
"""

def convert_string(string):
    cnt_zero = 0
    cnt_one = 0

    # 첫 번째 숫자 기준으로 그룹 개수 초기화
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