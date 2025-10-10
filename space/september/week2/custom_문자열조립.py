"""
문자열 조립

알파벳 대문자로 구성된 초기 문자 하나와 일련의 명령어가 주어집니다. 
각 명령어는 문자를 초기 문자열의 왼쪽 또는 오른쪽에 이어 붙이는 것을 의미합니다. 
모든 명령어를 수행하여 최종적으로 만들어진 문자열을 출력하는 함수를 작성하세요.

명령어는 방향과 문자로 구성됩니다.
- L: 왼쪽에 이어 붙이기
- R: 오른쪽에 이어 붙이기

- 입력
    - 첫째 줄에 초기 문자 C가 주어집니다.
    - 둘째 줄에 명령어의 개수 N이 주어집니다 (1 <= N <= 100,000).
    - 다음 N개의 줄에 걸쳐 각 명령어 방향 문자가 주어집니다.

- 출력
    - 모든 명령어를 수행한 후 완성된 최종 문자열을 출력하세요.

- 입력 예시
A
3
L B
R C
L D

- 출력 예시
DBAC
"""
import sys
from collections import deque

input = sys.stdin.readline

def addString(s, words):

    queue = deque([s])
    
    for word in words:
        # 삽입: O(1)
        if word[0] == "L":
            queue.appendleft(word[1])
        else:
            queue.append(word[1])
    
    return queue
        

# 입력 받기
s = input().rstrip() # 초기 문자
n = int(input())

words = []

for _ in range(n):
    words.append(list(input().split()))

result = addString(s, words)

# 문자열 붙일 경우 사용(리스트 -> 문자열)
final_string = "".join(result)
print(final_string)