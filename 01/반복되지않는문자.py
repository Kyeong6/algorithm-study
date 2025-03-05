def find_no_repeat_char(string):
    # 빈도수 확인
    occurrence_array = find_alphabet_occurrence_array(string)

    # 빈도수가 1인 알파벳들 중에서 string에 어떤 것이 먼저 나왔는지 파악 후 알파벳으로 반환
    not_repeat_char_array = list()
    
    for index in range(len(occurrence_array)):
        alphabet_occurrence = occurrence_array[index]
        if alphabet_occurrence == 1:
            not_repeat_char_array.append(chr(index + ord('a')))
    
    # 가장 먼저 나오는 알파벳 반환
    for char in string:
        if char in not_repeat_char_array:
            return char
    
    return "_"


        
def find_alphabet_occurrence_array(string):
    # 알파벳: 26
    alphabet_occurrence_array = [0] * 26

    # 빈도수 확인
    for char in string:
        # 문자가 아닌 경우 예외처리
        if not char.isalpha():
            continue
        arr_index = ord(char) - ord('a')
        alphabet_occurrence_array[arr_index] += 1
    
    return alphabet_occurrence_array


sentence = "abadabac"
print(find_no_repeat_char(sentence))