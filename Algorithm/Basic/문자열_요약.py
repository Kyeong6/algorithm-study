"""
방식: 알파벳의 개수를 뒤에 포함시켜야하기 때문에 아스키코드를 이용하여 해당 값을 얻고난 뒤 출력 결과 형식 구성
시간복잡도: O(N)
    - 단일 반복문 두 개 사용
"""
def summarized_string(string):
    # 알파벳 리스트
    alphabet_list = [0] * 26

    # 문자열 순회
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_list[arr_index] += 1

    # 출력결과 리스트
    result_list = list()

    # 값이 1 이상인 것을 확인 후 출력 결과 리스트 구성
    for i in range(len(alphabet_list)):
        if alphabet_list[i] >= 1:
            result = chr(i + ord('a')) + str(alphabet_list[i])
            result_list.append(result)

    # 출력 결과 형식 구성
    output = '/'.join(result_list)

    return output

test = "abbc"
print(summarized_string(test))