# def find_max_occurrence(string):
# 	# 알파벳: 26
# 	alphabet_occurrence_array = [0] * 26
	
# 	# 문자열도 반복문으로 하나씩 구분 가능
# 	for char in string:
# 		# 문자가 아닌 경우 예외처리
# 		if not char.isalpha():
# 			continue
# 		arr_index = ord(char) - ord('a')
# 		alphabet_occurrence_array[arr_index] += 1
		
# 	max_occurrence = 0
# 	max_alphabet_index = 0
	
# 	# 가장 빈도수가 많은 알파벳 추출
# 	for index in range(len(alphabet_occurrence_array)):
# 		alphabet_occurrence = alphabet_occurrence_array[index]
		
# 		if max_occurrence < alphabet_occurrence:
# 			max_occurrence = alphabet_occurrence
# 			max_alphabet_index = index
	
#     # 문자로 변환
# 	return chr(max_alphabet_index + ord('a'))	
	
# sentence = "hello my name is"
# print(find_max_occurrence(sentence))


# 위에 코드의 경우 동일한 빈도수일 경우 하나만 출력, 모두 출력 경우 풀어보기
def find_max_all_occurrence(string):
	# 알파벳: 26
	alphabet_occurrence_array = [0] * 26
	
	# 문자열도 반복문으로 하나씩 구분 가능
	for char in string:
		# 문자가 아닌 경우 예외처리
		if not char.isalpha():
			continue
		arr_index = ord(char) - ord('a')
		alphabet_occurrence_array[arr_index] += 1
	
	max_occurrence = max(alphabet_occurrence_array)

	# 가장 많이 등장한 알파벳 추출(동일 빈도 모두 출력)
	max_alphabets = [
		chr(index + ord('a')) for index, count in enumerate(alphabet_occurrence_array) if count == max_occurrence
	]

	return max_alphabets

sentence = "hello my name is"
print(find_max_all_occurrence(sentence))