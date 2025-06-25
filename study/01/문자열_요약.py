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

# test = "abbc"
# print(summarized_string(test))

"""
방식: 문자열 뒤집기 문제에서 사용한 방식 사용, 출력 형식인 '/' 사용을 위해 n-1번 반복
시간복잡도: O(N)
    - 단일 반복문
"""
def diff_summarized_string(string):
    n = len(string)
    cnt = 0
    result_str = ""

    for i in range(n-1):
        if string[i] == string[i+1]:
            cnt += 1
        else:
            result_str += string[i] + str(cnt + 1) + '/'
            cnt = 0
    
    result_str += string[n-1] + str(cnt + 1)

    return result_str

test = "acccdeee"
print(diff_summarized_string(test))