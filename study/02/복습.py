# 링크드 리스트 구현
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, value):
        cur = self.head

        # 다음 노드에 추가
        while cur.next != None:
            cur = cur.next
        
        cur.next = Node(value)

    def get_node(self, index):
        cur = self.head
        cur_index = 0

        while cur_index == index:
            cur = cur.next
            cur_index += 1
        
        return cur
    
    def add_node(self, index, value):
        new_node = Node(value)

        # index가 0일 경우 head 변경
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        
        # 노드 설정
        prev_node = self.get_node(index - 1)
        next_node = prev_node.next

        # 재연결
        prev_node.next = new_node
        new_node.next = next_node

    def delete_node(self, index):
        # index가 0일 경우 head 변경
        if index == 0:
            self.head = self.head.next

        prev_node = self.get_node(index - 1)
        delete_node = self.get_node(index)

        prev_node.next = delete_node.next


"""
이진 탐색 구현
"""
finding_target = 14
finding_numbers = list(range(1, 17))

def binary_search(target, numbers):
    cur_min = 0
    cur_max = len(numbers) - 1
    cur_mid = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if numbers[cur_mid] == target:
            return True
        elif numbers[cur_mid] < target:
            cur_min = cur_mid + 1
        else:
            cur_max = cur_mid - 1
        
        cur_mid = (cur_min + cur_max) // 2
    
    return False

# print(binary_search(finding_target, finding_numbers))

"""
1. 다음과 같은 두 링크드 리스트를 입력받았을 때, 합산한 값을 반환하시오
예를 들어 아래와 같은 링크드 리스트를 입력받았다면,
각각 678, 354 이므로 두 개의 총합
678 + 354 = 1032 를 반환해야 한다.
단, 각 노드의 데이터는 한자리 수 숫자만 들어갈 수 있다.
Test Case: [6] -> [7] -> [8]
           [3] -> [5] -> [4]
""" 
linked_list_01 = LinkedList(6)
linked_list_01.append(7)
linked_list_01.append(8)
linked_list_02 = LinkedList(3)
linked_list_02.append(5)
linked_list_02.append(4)

# 개별 링크드 리스트 합
def sum_link(link):
    total = 0
    cur = link.head

    while cur is not None:
        total = total * 10 + cur.data
        cur = cur.next

    return total

# 최종 합: 문제에서는 두 개만 입력값으로 사용했지만, 입력값의 크기를 제한하지않는 로직으로 변경
def final_sum(*links):
    total = 0
    for link in links:
        total += sum_link(link)

    return total

# print(final_sum(linked_list_01, linked_list_02))

"""
2. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
Test Case: [6] -> [7] -> [8]
"""
# 방법1: 링크드리스트의 값을 배열로 위치시켜 n-k번째 인덱스 값 출력
def find_used_index(link, k):
    cur = link.head
    link_value = []

    while cur is not None:
        link_value.append(cur.data)
        cur = cur.next

    n = len(link_value)
    result = link_value[n-k]

    return result


# 방법2: k라는 간격(길이)을 토대로 값 출력 -> used two pointer
def find_interval(link, k):
    fast = link.head
    slow = link.head

    # fast pointer를 k만큼 이동(간격 생성)
    for _ in range(k):
        fast = fast.next

    # fast pointer가 마지막 노드에 도달할 때 까지 수행
    while fast is not None:
        fast = fast.next
        slow = slow.next

    result = slow.data

    return result


link = linked_list_01
k = 2
# print(find_used_index(link, k))
# print(find_interval(link, k))

"""
# DFS 학습한 후 다시 풀어보기

3. 음이 아닌 정수들로 이루어진 배열이 있다. 이 수를 적절히 더하거나 빼서 특정한 숫자를 만들려고 한다.
예를 들어 [1, 1, 1, 1, 1]로 숫자 3을 만들기 위해서는 다음 다섯 방법을 쓸 수 있다.
-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

사용할 수 있는 숫자가 담긴 배열 numbers, 타겟 넘버 target_number이 매개변수로 주어질 때
숫자를 적절히 더하고 빼서 타겟 넘버를 만드는 방법의 수를 반환하시오.
Test Case:
numbers = [1, 1, 1, 1, 1]
target_number = 3
numbers = [4,1,2,1]
target_number = 4
"""


"""
4. 다음과 같이 숫자로 이루어진 배열이 있을 때, 
2이 존재한다면 True 존재하지 않는다면 False 를 반환하시오.
Test Case: [0, 3, 5, 6, 1, 2, 4]
"""
# 정렬 후 이진탐색 진행: O(NlogN) + O(logN) = O(NlogN)
def is_existing_number(target, numbers):
    # 이진탐색을 위한 정렬
    numbers = sorted(numbers)

    cur_min = 0
    cur_max = len(numbers) - 1
    cur_mid = (cur_min + cur_max) // 2

    while cur_min <= cur_max:
        if numbers[cur_mid] == target:
            return True
        elif numbers[cur_mid] < target:
            cur_min = cur_mid + 1
        else:
            cur_max = cur_mid - 1
        
        cur_mid = (cur_min + cur_max) // 2

target = 2
test = [0, 3, 5, 6, 1, 2, 4]
# print(is_existing_number(target, test))

"""
5. 배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
Test Case: 
menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]
"""
def is_ordered(menus, orders):
    # 존재 유무 확인에 적합한 자료구조? -> 집합(해시 테이블 사용)
    # : O(n)
    menus = set(menus)

    # 주문 목록 조회: O(m)
    for order in orders:
        # 집합에서 존재 유무 확인: O(1)
        if order not in menus:
            return False
    
    return True


menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]
# print(is_ordered(menus, orders))

"""
6. 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
Test Case: 7 3
Output: <3, 6, 2, 7, 5, 1, 4>
"""
from collections import deque

# 링크드 리스트 사용(삽입/삭제 과정 존재하여 시간복잡도 최적화)
# 해당 문제처럼 나열했을 때 돌려야하는(rotate) 과정이 존재하면 해당 접근법 사용
def josephus_used_linked_list(n, k):
    # 배열 생성
    array = [x for x in range(1, n+1)]

    # deque를 이용한 Linked list 생성
    link = deque(array)

    # 결과값 배열
    result_list = []

    while len(link) != 0:
        # k-1개를 돌려야지 해당 k값 제거 가능
        link.rotate(-(k-1))
        # 맨 앞으로 나온 값 제거 및 결과값 배열에 적재
        result_list.append(link.popleft())

    # print(result_list)

    # 출력 형식: result_list는 수치형 데이터이므로 map을 통한 모든 데이터 str형으로 변경
    output = "<" + ", ".join(map(str,result_list)) + ">"
    
    return output


def josephus_used_list(n, k):
    # 배열 생성
    people = [x for x in range(1, n+1)]

    # 결과값 리스트
    result_list = []

    next_index = k-1

    # 반복
    while people:
        # 특정 인덱스 값 제거
        result = people.pop(next_index)
        result_list.append(result)
        if len(people) != 0:
            # 리스트 기반 원형 순환 구조(이해 필요)
            next_index = (next_index + (k-1)) % len(people)
    
    output = "<" + ", ".join(map(str, result_list)) + ">"
    
    return output


n = 7
k = 3
# print(josephus_used_linked_list(n, k))
# print(josephus_used_list(n, k))

"""
7. 0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.
Test Case: 10
Output: 3628800
"""
def factorial(number):
    
    if number == 1:
        return 1

    return number * factorial(number -1)


number = 10
# print(factorial(number))

"""
8. 단순 회문검사 
Test Case: addda
"""
def palindrome(string):
    n = len(string)
    for i in range(n):
        # 앞뒤 비교
        if string[i] != string[n-1-i]:
            return False
    
    return True

# 재귀를 통한 잘라가기, 즉 분할 수행
def recursion_palindrome(string):
    
    if string[0] != string[-1]:
        return False
    
    if len(string) <= 1:
        return True
    
    # 재귀(문자열 자르기)
    return recursion_palindrome(string[1:-1])

test = "addda"
# print(palindrome(test))
# print(recursion_palindrome(test))


"""
9. 회문은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열울 말한다.
만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면
우리는 이런 문자열을 유사회문이라고 부른다. 
만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다.
Test Case: 
7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc
"""
import sys
input = sys.stdin.readline

def semi_palindrome(string, s, e, chance):
    # two pointer
    while s < e:
        # 문자가 다를 경우(pointer의 값이 다를 경우)
        if string[s] != string[e]:
            # 삭제 기회 존재(유사회문)
            if chance == 0:
                # chance가 0일경우 한 번의 기회가 주어지는데, 이때 나누어서 수행할 수 있음 -> 재귀
                # 왼쪽 혹은 오른쪽 삭제하는 두 가지 경우 중 하나라도 존재하면 유사회문
                skip_start = semi_palindrome(string, s+1, e, 1)
                skip_end = semi_palindrome(string, s, e-1, 1)
                if skip_start == 0 or skip_end == 0:
                    return 1
                else:
                    return 2
            else:
                return 2
        s += 1
        e -= 1

    return 0

def is_palindrome(string):
    return semi_palindrome(string, 0, len(string) - 1, 0)

# 사용자 입력
n = int(input().strip())
words = [input().strip() for _ in range(n)]

# 결과 출력
for word in words:
    print(is_palindrome(word))