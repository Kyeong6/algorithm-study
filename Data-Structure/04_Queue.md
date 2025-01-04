## 큐(Queue)

- 큐는 FIFO(First In, First Out), 즉 "선입선출"인 자료구조이다.
- 큐는 데이터가 입력되는 순서대로 처리하고 싶을 때 사용하면 매우 효율적이다. 왜냐하면 큐는 "O(1)", 즉 상수 시간에 값을 넣고 뺄 수 있다.
- python에서는 ‘collection’ 내장 모듈의 ‘deque’을 사용

```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)
queue.append(3) # [1,2,3]

queue.popleft() # [1,2]
queue.popleft() # [1]
queue.popleft()
```

### 너비 우선 탐색

- 큐는 트리, 그래프를 너비 우선 탐색할 때 많이 사용

```python
from collections import deque

def bfs(root, target):
	if root is None:
		return False
		
	queue = deque([root])
	while queue:
		node = queue.popleft()
		if node.val == target:
			return True
		queue += [node.left, node.right]
	return False
```

### 우선순위 큐

- 큐에 특수한 형태로는 우선순위 큐 자료구조가 존재한다. 먼저 추가한 값이 먼저 삭제되지 않고 우선순위가 제일 높은 값이 가장 먼저 삭제된다.
- 데이터를 내부적으로 정렬된 상태로 유지하기 때문에 우선순위 큐에 값을 추가하거나 삭제할 때는 ‘O(log n)’시간이 소모된다.

### 큐(queue) 자료구조 사용

- list

```python
queue = [4,5,6]
queue.append(7) # [4,5,6,7]

# pop(index) : 해당 인덱스값 삭제
queue.pop(0) # [5,6,7]
```

list를 사용한 후 append, pop을 사용하면 뒤에서 데이터가 추가되고, 앞에서 데이터가 삭제가 되기 때문에 Queue 자료구조와 동일하다. 

참고로 앞에 데이터를 넣고 뒤에 데이터를 삭제하는 것은 다음과 같다.

```python
queue = [4,5,6]
queue.insert(0, 2) # [2,4,5,6]
queue.pop() # [2,4,5]
```

큐 자료구조의 효과를 얻기위해서 리스트를 사용하는 것은 성능 측면에서 추천되지 않는다. 인덱스를 통해서 무작위로 접근하는 데 최적화 되어있기 때문에 pop(), insert()에 인덱스 0을 넣는 것은 시간복잡도 ‘O(n)’이기 때문에 리스트에 담고 있는 개수가 많아질 수록 성능이 좋지 않아진다. 

왜냐하면, 첫 번째 인덱스의 값 데이터를 삭제하면 뒤에 있는 것들을 앞으로 당겨줘야 하기 때문이다. 같은 원리로 맨 앞에 데이터를 적재한다면, 기존 값들을 모두 하나씩 뒤로 밀어야하기 때문이다.

즉, 성능을 높여야하는 애플리케이션에서는 리스트를 큐처럼 사용하는 것은 좋지 않은 방식이다. 

- deque

```python
from collections import deque

# deque 객체 생성
queue = deque([4,5,6])

queue.append(7) # deque([4,5,6,7]) : deque 객체로 배열 존재
queue.popleft() # deque([5,6,7])
```

deque 객체를 통한 연산인 append, popleft를 통해서 오른쪽(마지막)에 데이터가 적재가 되고, 왼쪽(처음)부터 데이터가 제거되는 것을 확인할 수 있다. 

이렇게 deque 객체를 이용한 데이터 추가 및 제거는 시간복잡도 ‘O(1)’이기 때문에 리스트를 이용했을 때보다 좋은 성능을 보일 수 있다. 

하지만 내부적으로 linked list를 사용하고 있기 때문에, 인덱스로 무작위 접근을 하고자 할 때 맨 앞이나 맨 뒤에서부터 i번째 탐색을 통해서 접근할 수 있다. 

- Queue(클래스)

```python
from queue import Queue

que = Queue()

que.put(4)
que.put(5)
que.put(6)
que.get() # 4 추출
que.get() # 5 추출
que.get() # 6 추출
```

큐 클래스로, 멀티 쓰레딩 환경에서 사용되며 내부적으로 Locking을 지원하여 여러 개의 쓰레드가 동시에 데이터를 추가 및 삭제가 가능하다. 

list나 deque와 달리 방향성이 없기 때문에 데이터의 추가 및 삭제가 하나의 메서드로 사용된다

- put : 추가
- get : 추출

Queue는 deque처럼 ‘O(1)’의 성능을 보이는데, list나 deque와 달리 인덱스를 통한 접근을 기본적으로 지원하지 않음, 즉 추가 / 추출만 자유롭게 가능(put, get의 인자에 인덱스를 안 넣는다는 의미)

### 우선순위 큐(PriorityQueue) 사용(Heap)

우선순위 큐는 데이터를 추가한 순서대로 제거하는 선입선출 특성을 가진 일반적인 큐의 자료구와 달리, **데이터 추가는 어떤 순서로 해도 상관이 없지만, 제거될 때는 가장 작은 값을 제거하는 특성을 지닌 자료구조**이다.

이 말은 내부적으로 데이터를 정렬된 상태로 보관하는 메커니즘이 존재한다는 뜻이다. 

```python
from queue import PriorityQueue

# 우선순위 큐 객체 생성
queue = PriorityQueue()

# 우선순위 큐 크기 설정
que = PriorityQueue(maxsize=8)

que.put(4)
que.put(1)
que.put(7)
que.put(3)
# 결과 : [1,3,4,7]

print(que.get()) # 1
print(que.get()) # 3
print(que.get()) # 4
print(que.get()) # 7
```

put 메서드를 이용해서 넣을 경우 우선순위 큐 원칙에 따라 자동으로 정렬되어, get 메서드를 사용하면 작은 순서대로 추출됨을 확인할 수 있다. 

```python
que.put((3, 'Apple'))
que.put((1, 'Banana'))
que.put((2, 'Cherry'))

print(que.get()[1]) # Banana
print(que.get()[1]) # Cherry
print(que.get()[1]) # Apple
```

만약 단순 오름차순이 아닌 다른 기준으로 원소가 정렬되기를 원한다면, (우선순위, 값)의 튜플 형태로 데이터를 추가하고 제거하면 된다. (값이 1번 인덱스이므로 get()[1] 사용)

참고로 기본적인 큐같은 경우는 삽입/삭제가 ‘O(1)’이었지만, 우선순위 큐 삽입/삭제는 정렬이 포함되기 때문에 ‘O(log n)’의 시간복잡도를 가진다. 

![스크린샷 2024-12-30 오후 2 24 02](https://github.com/user-attachments/assets/0b5ac92a-1327-41ae-9730-61991eebb03e)