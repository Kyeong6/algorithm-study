# 리스트 컴프리헨션을 이용한 2차원 배열 생성
arr = [[i]*4 for i in range(3)]
print(arr)

# 맨 뒤 데이터 삽입: O(1)
my_list = [1,2,3]
my_list.append(4) # [1,2,3,4]

# 중간에 데이터 삽입: O(N)
my_list = [1,2,3,4,5]
my_list.insert(2, 100) # [1,2,100,4,5]

# 특정 위치 데이터 팝: 처음/중간 -> O(N)
my_list = [1,2,3,4,5]
popped_element = my_list.pop(2) # 3

# 특정 데이터 삭제: 처음/중간 -> O(N)
my_list = [1,2,3,4,5]
my_list.remove(2) # [1,2,4,5]

"""
자주 사용되는 리스트 연관 메서드
len(): 리스트 전체 데이터 개수 반환
index(): 처음 등장한 인덱스 반환
sort(): 오름차순 / 내림차순으로 데이터 정렬
count(): 특정 데이터 개수 반환
"""
fruits = ["apple", "banana", "cherry", "apple", "orange", "banana", "kiwi"]
len(fruits) # 7
fruits.index("banana") # 1
fruits.sort()
fruits.count("apple") # 2

