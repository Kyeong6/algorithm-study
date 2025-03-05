"""
1. 최댓값 찾기
Q. 다음과 같이 숫자로 이루어진 배열이 있을 때, 이 배열 내에서 가장 큰 수를 반환하시오.
Test Case: [3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 43]
"""
def find_max_value(array):
    # 최댓값 초기화
    max_num = array[0]
    # 탐색을 통한 최댓값 비교 진행
    for i in range(1, len(array)):
        if array[i] > max_num:
            max_num = array[i]
        
    return max_num

# first_test_case = [3, 5, 6, 1, 2, 4, 3, 5, 6, 1, 2, 43]
# print(find_max_value(first_test_case))
# second_test_case = [4, 51, 26, 31, 62, 24, 13, 5, 6, 1, 2, 43]
# print(find_max_value(second_test_case))

"""
2. 최빈값 찾기
Q.  다음과 같은 문자열을 입력받았을 때, 어떤 알파벳이 가장 많이 포함되어 있는지 반환하시오. 
(단 최빈값을 가진 알파벳이 여러개일 경우 알파벳 순서가 가장 앞에 위치한 알파벳을 출력하시오)
Test Case: "hello my name is coding"
"""
def find_max_occurrence(string):
    # 빈도수 체크를 위한 알파벳 리스트 생성
    alphabet_list = [0] * 26

    # 인덱스 생성: 아스키코드를 이용한 알파벳(문자) 수치화
    for char in string:
        # 문자가 아닐 경우 패스
        if not char.isalpha():
            continue
        # 인덱스 생성 및 카운팅 진행
        arr_index = ord(char) - ord('a')
        alphabet_list[arr_index] += 1

    # 가장 많은 빈도수의 알파벳 찾기
    max_occurrence = 0
    max_occurrence_index = 0

    for i in range(len(alphabet_list)):
        if max_occurrence < alphabet_list[i]:
            max_occurrence = alphabet_list[i]
            max_occurrence_index = i 
    
    return chr(max_occurrence_index + ord('a'))

# first_test_case = "hello my name is coding"
# print(find_max_occurrence(first_test_case))

"""
3. 곱하기 or 더하기
Q. 다음과 같이 0 혹은 양의 정수로만 이루어진 배열이 있을 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 
'✕' 혹은 '+' 연산자를 넣어 결과적으로 가장 큰 수를 구하는 프로그램을 작성하시오. 

단, '+' 보다 '✕' 를 먼저 계산하는 일반적인 방식과는 달리, 모든 연산은 왼쪽에서 순서대로 이루어진다.
Test Case: [0, 3, 5, 6, 1, 2, 4]
"""
def multiplier_plus(array):
    sum = 0
    # sum은 이전의 계산 결과, number은 현재 숫자
    for number in array:
        if number <= 1 or sum <= 1:
            sum += number
        else:
            sum *= number
    
    return sum

# first_test_case = [0, 3, 5, 6, 1, 2, 4]
# print(multiplier_plus(first_test_case))

"""
4. 반복되지 않는 문자
Q. 다음과 같이 영어로 되어 있는 문자열이 있을 때, 
이 문자열에서 반복되지 않는 첫번째 문자를 반환하시오. 만약 그런 문자가 없다면 _ 를 반환하시오.
Test Case: "abadabac"
"""
def find_not_repeat(string):
    alphabet_list = [0] * 26

    # 횟수 체크
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_list[arr_index] += 1

    # 횟수가 1인 문자 포함 배열
    not_repeat_chars = []

    # 횟수 배열 탐색 후 값이 1인 인덱스 추출 및 문자 변환 진행
    for i in range(len(alphabet_list)):
        if alphabet_list[i] == 1:
            char = chr(ord('a') + i)
            not_repeat_chars.append(char)
    
    # 반복되지 않는 문자가 존재하지 않을 경우
    if len(not_repeat_chars) == 0:
        return "_"

    return not_repeat_chars[0]

# first_test_case = "abadabac"
# print(find_not_repeat(first_test_case))
# second_test_case = "abcabchwc"
# print(find_not_repeat(second_test_case))
# thrid_test_case = "abcabcabc"
# print(find_not_repeat(thrid_test_case))

"""
5. 소수 찾기
Q. 정수를 입력 했을 때, 그 정수 이하의 소수를 모두 반환하시오. 
소수는 자신보다 작은 두 개의 자연수를 곱하여 만들 수 없는 1보다 큰 자연수이다.
Test Case: 입력 - 20, 출력 - [2, 3, 5, 7, 11, 13, 17, 19]
"""
def find_decimal(number):
    # 소수 리스트
    decimal_lst = []

    # 소수는 2와 3으로 나눌 수 없음
    for i in range(2, number+1):
        # 찾았던 소수들로만 나누어서 확인
        for decimal in decimal_lst:
            # 연산 횟수를 줄이기 위한 소수의 성질 이용
            if (i % decimal == 0) and decimal * decimal <= i:
                break
        else:
            decimal_lst.append(i)

    return decimal_lst

# test_case = 20
# print(find_decimal(test_case))

"""
6. 문자열 뒤집기
Q. 
0과 1로만 이루어진 문자열이 주어졌을 때, 이 문자열에 있는 모든 숫자를 전부 같게 만들려고 한다. 
할 수 있는 행동은 문자열에서 연속된 하나 이상의 숫자를 잡고 모두 뒤집는 것이다. 뒤집는 것은 1을 0으로, 0을 1로 바꾸는 것을 의미한다.
주어진 문자열을 모두 0 혹은 모두 1로 같게 만드는 최소 횟수를 반환하시오.
Test case: "0001100"
"""
def reverse_string(string):
    # 바뀌는 횟수 지정
    change_one = 0 # 0 -> 1
    change_zero = 0 # 1 -> 0

    # 첫번째 숫자 기준으로 그룹 개수 초기화
    if string[0] == "0":
        change_one += 1
    elif string[0] == "1":
        change_zero += 1

    # 문자열 순회하며 변환 발생 지점 찾기
    for i in range(len(string)-1):
        if string[i] != string[i+1]:
            if string[i+1] == "0":
                change_one += 1
            if string[i+1] == "1":
                change_zero += 1
    
    # 최소한의 뒤집기 횟수 반환
    return min(change_one, change_zero)

# first_test_case = "0001100"
# print(reverse_string(first_test_case))
# second_test_case = "000011101010"
# print(reverse_string(second_test_case))

"""
7. 문자열 요약
Q.
1. 입력으로 소문자의 알파벳 순으로 정렬된 문자열이 입력됩니다.
2. 각 알파벳은 중복이 가능합니다.
3. 중간에 없는 알파벳이 있을 수도 있습니다.

입,출력 예시와 같이 입력 문자열에 나타나는 각 알파벳의 종류,갯수를 요약하여 나타내시오.
Test Case: 
abc 	# a1/b1/c1
aaabbbc	# a3/b3/c1
"""
def summarize_string(string):
    # 개수 파악을 위한 알파벳 리스트 생성
    alphabet_list = [0] * 26

    # 문자 카운팅 진행
    for char in string:
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_list[arr_index] += 1
    
    # 출력을 위한 리스트 생성
    output_list = []
    
    # 출력 형식 지정
    for i in range(len(alphabet_list)):
        if alphabet_list[i] > 0:
            char = chr(ord('a') + i)
            output = char + str(alphabet_list[i])
            output_list.append(output)
    
    # "/" 구분자를 이용해서 출력 구성
    final_output = "/".join(output_list)

    return final_output

# first_test_case = "abc"
# print(summarize_string(first_test_case))
# second_test_case = "aaabbbc"
# print(summarize_string(second_test_case))