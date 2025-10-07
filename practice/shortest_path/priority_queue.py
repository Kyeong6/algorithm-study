"""
- 우선순위 큐 : 가장 우선순위가 높은 데이터
- 힙(Heap)
    - 최소 힙 : 값이 낮은 데이터부터 꺼냄
    - 최대 힙 : 값이 높은 데이터부터 꺼냄
    - 리스트 삽입/삭제 시간 복잡도 : O(1) / O(N)
    - 힙 삽입/삭제 시간 복잡도 : O(logN) / O(logN)

- 정렬한다면 O(NlogN)만에 가능(python library sort와 동일)
"""

# 최소 힙
import heapq

# 오름차순 힙 정렬(Heap Sort)
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

array = [1,3,5,7,9,2,4,6,8,0]
result = heapsort(array)
print(result)

# 최대 힙
def heapsort_max(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(-heapq.heappop(h))
    return result

result = heapsort_max(array)
print(result)