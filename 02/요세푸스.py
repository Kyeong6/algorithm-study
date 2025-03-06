"""
Q. 1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 
이제 순서대로 K번째 사람을 제거한다. 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 
이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 
예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.

N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.
Test Case: 7 3
Output: <3, 6, 2, 7, 5, 1, 4>
"""
import sys
input = sys.stdin.readline()

# 리스트 이용
def josephus(n, k):
    result_arr = []

    next_index = k - 1
    people_arr = list(range(1, n+1))

    # 반복: O(n)
    while people_arr:
        # 특정 인덱스 값 제거: O(n)
        result = people_arr.pop(next_index)
        result_arr.append(result)
        if len(people_arr) != 0:
            next_index = (next_index + (k-1)) % len(people_arr)

    print("<", ", ".join(map(str, result_arr)), ">", sep='')

n, k = map(int, input.split())
josephus(n, k)      
"""
방식: 리스트를 이용한 원형 순환 처리를 사용하여 풀이 진행
시간복잡도: O(n^2)
    - 탐색 및 pop 메서드 사용
"""

from collections import deque

def josephus_linked_list(n, k):
    # 생성: O(n)
    people = deque(range(1, n + 1))
    
    result = []
    
    # 반복: O(n)
    while people:
        # k-1만큼 회전(-가 존재하여 왼쪽 회전) (k번째가 앞에 오도록): O(k)
        people.rotate(-(k-1))  
        # k번째 사람 제거: O(1)
        result.append(people.popleft())  

    print("<", ", ".join(map(str, result)), ">", sep='')

# 실행
n, k = 7, 3
josephus_linked_list(n, k)
"""
방식: deque를 이용한 링크드리스트 방식 사용
    - rotate 메서드를 이용한 회전 원리 이용
시간복잡도: O(n)
    - deque를 이용한 링크드리스트 이용
    - list와 달리 제거 과정에서 O(1) 소요
"""