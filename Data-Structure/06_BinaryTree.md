## 개념 정리

### 이진 트리란?

- 트리 자료구조의 한 형태로 각 노드가 최대 2개의 자식 노드를 가질 수 있음

```python
    3
   / \
  9  20
    /  \
   15   7
     \
      4
```

- 위의 예시처럼 이진 트리는 노드의 자식의 개수가 0개, 1개, 2개가 될 수 있음
- 링크드 리스트와 같이 모든 노드의 자식이 1개인 트리도 유효한 이진 트리가 될 수 있음

```python
    3
   /
  9
 /
15
 \
  4
```

- 이진 트리의 좀 더 특수한 형태로 이분 탐색 트리(Binary Search Tree)라는 것도 존재
    - 노드의 값을 정렬된 형태로 유지하기 위해서 한 가지 더 조건이 강제됨
    - 왼쪽 트리에 있는 모든 노드의 값은 부모 노드의 값보다 작아야하고, 오른쪽 트리에 있는 모든 노드의 값은 부모 노드의 값보다 커야 함
    - **이진 탐색의 조건이 정렬 되어야하기 때문에 필요 !**

```python
    3
   / \
  1   9
     /  \
    4   15
     \
      7
```

### 트리 노드

- 보통 트리의 최상단(root)노드가 입력으로 주어짐
    - 이진 트리는 최대 2개의 자식을 가질 수 있기 때문에 자식을 가리키는 두 개의 포인터가 필요
    - left는 좌측 자식, right는 우측 자식을 가리키고 val은 노드에 저장되는 값을 나타냄

```python
class TreeNode:
	def __init__(self, val=0, left=None, right=None):
		self.val = val
		self.left = left
		self.right = right
```

### 트리 탐색

- 트리에서 원하는 값을 찾을 때는 크게 두 가지 접근 방법 사용
- DFS : 재귀 / 반복(Stack)

```python
# 재귀 알고리즘
def dfs(node, target):
	if node is None:
		return False
	if node == target:
		return True
	return dfs(node.left, target) or dfs(node.right, target)
```

```python
# 반복 알고리즘: Stack 사용
def dfs(root, target):
	if root is None:
		return False
	stack = [root]
	while stack:
		node = stack.pop()
		if node.val = target:
			return True
		stack += [node.left, node.right]
	return False
```

- BFS: Queue

```python
# 반복 알고리즘: Queue 사용
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

### 트리 순회

- 트리 내의 모든 노드를 특정 순서로 방문하는 것을 트리 순회(traversal)이라고 함
    - 전위 순회(pre-order)
    - 중위 순회(in-order)
    - 후위 순회(post-order)
    - 모두 재귀 알고리즘으로 구현 가능하고 부모 노드 기준으로 전/중/후 결정됨
- 전위 순회(pre-order): 코딩 테스트에서 트리를 순회할 때 가장 흔하게 사용되는 방식

```python
def pre_order(node):
	print(node.val)
	pre_order(node.left)
	pre_order(node.right)
```

- 중위 순회(in-order): 이진 탐색 트리의 경우 중위 순회를 하면 **오름차순으로 모든 노드 방문한다는 특징** 존재

```python
def in_order(node):
	in_order(node.left)
	print(node.val)
	in_order(node.right)
```

- 후위 순회(post-order)

```python
def post_order(node):
	post_order(node.left)
	post_order(node.right)
	print(node.val)
```