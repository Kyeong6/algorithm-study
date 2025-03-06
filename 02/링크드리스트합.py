"""
Q. 다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오
예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
각각 678, 354 이므로 두 개의 총합
678 + 354 = 1032 를 반환해야 한다.
단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.
Test Case: [6] -> [7] -> [8]
           [3] -> [5] -> [4]
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        while cur.next != None:
            cur = cur.next
            
        cur.next = Node(value)

    # 출력 확인 메서드
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

# Linked List 생성
linked_list_1 = LinkedList(6)
linked_list_1.append(7)
linked_list_1.append(2)
# linked_list_1.print_all()
linked_list_2 = LinkedList(3)
linked_list_2.append(5)
linked_list_2.append(4)
# linked_list_2.print_all()

# 합 계산 로직
def get_linked_lst_sum(link):
    sum = 0
    cur = link.head

    while cur is not None:
        sum = sum * 10 + cur.data
        cur = cur.next

    return sum

# 두 링크드 리스트 합 계산 함수
def add_linked_list(link1, link2):
    
    sum_1 = get_linked_lst_sum(link1)
    sum_2 = get_linked_lst_sum(link2)    

    result = sum_1 + sum_2

    return result

print(add_linked_list(linked_list_1, linked_list_2))


"""
방식: 링크드 리스트 구현 후 합을 구하는데, 이때 "sum = sum * 10 + cur_1.data" 방식 유의해서 보기
    - 처음에는 문자의 합을 이용하여 최종적으로 int()로 변환하려 했으나, 위의 방식이 더 효율적(공간 복잡도)
시간복잡도: O(m + n)
    - 다른 두 종류의 while문 사용
"""

