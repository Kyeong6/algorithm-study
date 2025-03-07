"""
Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
Test Case: [6] -> [7] -> [8]

방식: 두 가지 방식 사용
    - 링크드리스트 값을 리스트(배열)에 담아 조회(O(1))를 이용하여 값 추출
    - 투 포인터(slow, fast)를 이용한 간격을 사용하여 풀이 진행
시간복잡도: 두 방식 모두 O(n)
"""
# Node 정의
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Linked List 정의
class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
    
    def append(self, value):
        cur = self.head

        while cur.next != None:
            cur = cur.next
        
        cur.next = Node(value)

    # 뒤에서 K번째 값 출력 함수
    def get_value(self, k):
        # node 값 적재 리스트
        node = []
        cur = self.head

        # 반복: O(n)
        while cur != None:
            # 값 추가: O(1) -> 동적 리스트 원리
            node.append(cur.data)
            cur = cur.next
        n = len(node)

        # 값 조회: O(1)      
        value = node[n-k]

        return value
    
    # 또 다른 방법: 투 포인터 사용
    def get_value_pointer(self, k):
        slow = self.head
        fast = self.head

        # K만큼의 거리를 유지하기 위한 fast 이동
        for i in range(k):
            fast = fast.next
        
        # slow와 fast 간격은 K만큼 유지
        while fast is not None:
            slow = slow.next
            fast = fast.next
        
        return slow.data

    
linked_list = LinkedList(6)
linked_list.append(7)
linked_list.append(8)
k = 2
print(linked_list.get_value(k))
print(linked_list.get_value_pointer(k))
