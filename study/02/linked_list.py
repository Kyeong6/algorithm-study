# Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
# [5] -> [12] -> [7] -> [6] 연결
first_node = Node(5)
second_node = Node(12)
first_node.next = second_node
third_node = Node(7)
second_node.next = third_node
fourth_node = Node(6)
third_node.next = fourth_node

# Linked List
class LinkedList:
    def __init__(self, value):
        # 맨 앞 노드
        self.head = Node(value)

    # 연결 메서드
    def append(self, value):
        cur = self.head

        # 마지막 노드 pointer x
        while cur.next != None:
            cur = cur.next
        
        cur.next = Node(value)
    
    # 출력 확인 메서드
    def print_all(self):
        cur = self.head
        while cur is not None:
            print(cur.data)
            cur = cur.next

    # 반환 메서드 
    def get_node(self, index):
        cur = self.head
        cur_index = 0

        # 이동
        while cur_index != index:
            cur = cur.next
            cur_index += 1

        return cur
    
    # 삽입 메서드
    def add_node(self, index, value):
        new_node = Node(value)

        # index가 0일 경우, head 변경
        if index == 0:
            new_node.next = self.head
            self.head = new_node

        # 삽입해야할 노드 이전 노드 확인
        prev_node = self.get_node(index - 1)

        # 연결 끊기 전 기존 next node 저장 필요
        next_node = prev_node.next

        # 재연결 진행
        prev_node.next = new_node
        new_node.next = next_node
    
    # 삭제 메서드
    def delete_node(self, index):
        # index가 0일 경우, head 변경
        if index == 0:
            self.head = self.head.next
            return

        # 삭제될 노드 이전 노드 확인
        prev_node = self.get_node(index - 1)

        # 삭제할 노드
        del_node = self.get_node(index)

        # 재연결 진행
        prev_node.next = del_node.next




linked_list = LinkedList(5)
linked_list.append(12)
linked_list.append(7)
linked_list.append(6)
linked_list.print_all()
# print(linked_list.get_node(3).data)
linked_list.add_node(1, 4)
linked_list.delete_node(0)
linked_list.print_all()