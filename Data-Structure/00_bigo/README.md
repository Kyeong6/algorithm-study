## 시간 복잡도

- 함수의 실행시간을 **Step 수**로 간주하자!
- 각 함수를 수행하기 위한 행(Line)은 “상수(고정된 값)”라고 가정
- 실행시간이 aN + b라고 가정해보자
    - N이 무한대일 때가 판단의 근거인데 최고차항만 의미가 있고, 계수가 영향이 없는 것을 “점근적 분석”이라고 함
- 점근적 분석은 어떤 함수에 근접하나?를 수식을 표현한 것
- 중요한 건 시간 복잡도는 입력값에 따라 Step이 어느 정도 걸리느냐를 표현한 것!
    - 예를 들어 O(1) 같은경우 상수시간으로 입력 사이즈와 상관없이 Step이 일정한 알고리즘
    
    ```python
    n = int(input())
    
    for i in range(n):
    	print("hi")
    ```

### O(1) : constant time

- 입력 데이터의 크기와 상관없이 언제나 일정한 시간이 걸리는 알고리즘

```python
lst = list()
if (lst[0] == 0):
	return True
```

- 배열이 얼마나 큰지와 상관없이 언제나 일정한 속도로 결과를 반환

![스크린샷 2024-12-30 오후 3 54 25](https://github.com/user-attachments/assets/f8a72beb-565f-4053-94b8-845d247da6e5)

- 데이터가 증가함에 따라 성능의 변화가 없는 것을 그래프로 확인할 수 있음

### O(n): linear time

- 입력 데이터의 크기에 비례해서 처리 시간이 걸리는 알고리즘을 표현할 때 사용

```python
for i in range(n):
	print(i)
```

- n개의 데이터를 받으면 n번 루프를 돌기 때문에 n이 하나씩 늘어날 때마다 처리가 하나 씩 늘어남

![스크린샷 2024-12-30 오후 3 56 22](https://github.com/user-attachments/assets/bcfadaa0-bf84-4696-b30c-1b336e6ebc0b)

- 데이터가 증가함에 따라 비례해서 처리 시간도 증가함을 확인할 수 있음
- 데이터와 시간이 같은 비율로 증가하기 때문에 그래프는 직선으로 표현이 됨

### O(n^2): quadratic time

```python
for i in range(n):
	for j in range(n):
		print(i+j)
```

- n을 통해서 loop를 돌렸는데, 또 n으로 loop를 또 돌렸을 때 발생
- n개의 데이터를 받으면 첫 번째 루프에서 n번 돌면서 각각의 엘리먼트에서 n번씩 또 도니까 처리횟수가 n을 가로,세로 길이로 가지는 면적만큼 되는 것이다!
    - n이 커질수록 가로, 세로 각각 한 줄씩 늘어나니까 데이터가 많아질수록 데이터의 처리 시간도 오래 걸릴 것이다(면적만큼 처리시간 걸림)

![스크린샷 2024-12-30 오후 4 01 09](https://github.com/user-attachments/assets/7c9ef09d-9e27-48fd-8a30-149e956af1f6)

![스크린샷 2024-12-30 오후 4 01 22](https://github.com/user-attachments/assets/ad0a76bf-2654-41a8-9d2d-8fa7552b20a7)

### O(nm): quadratic time

```python
for i in range(m):
	for j in range(n):
		print(i+j)
```

- 위의 O(n^2)와 비슷하지만, m을 n만큼 돌리기 때문에 서로 다르다
    - m ≠ n이므로 헷갈릴 수 있음

![스크린샷 2024-12-30 오후 4 03 10](https://github.com/user-attachments/assets/6bb3390b-3ee9-4ffe-970e-3ada094066c2)

![스크린샷 2024-12-30 오후 4 03 35](https://github.com/user-attachments/assets/c133b6cd-b51a-45c2-b7ba-331600530c61)

- 변수가 다르다면 Big O에도 다르게 표시해줘야 한다

### O(n^3): polynomial time

```python
for i in range(n):
	for j in range(n):
		for k in range(n):
			print(i+j+k)
```

![스크린샷 2024-12-30 오후 4 04 46](https://github.com/user-attachments/assets/bf318142-7eec-413a-9a03-f045bf03b73b)

- n^3이므로 큐브 모양이 됨

![스크린샷 2024-12-30 오후 4 05 12](https://github.com/user-attachments/assets/2c3835ae-8b2c-4092-80d0-832334b6eae1)

- O(n^2)보다 데이터가 적을 때 더 많은 시간이 걸림을 확인할 수 있음

### O(2^n): exponential time

- 피보나치 수열을 기하학적으로 생각하면 길이가 1인 사각형을 기준으로 연결해서 다른 사각형을 만드는 것이다!

![스크린샷 2024-12-30 오후 4 07 03](https://github.com/user-attachments/assets/bdc543d7-1ef9-44a9-926b-95d5a65cfb47)

![스크린샷 2024-12-30 오후 4 07 16](https://github.com/user-attachments/assets/5f60ca4b-c8b2-4de1-a59c-f78b8eca28d8)

- 피보나치를 통해 피보나치 나선형인 황금비율을 얻을 수 있음
- 재귀함수를 이용한 피보나치 구현

```python
def fibo(n):
	if (n <= 0):
		return
	elif (n == 1) or (n == 2):
		return 1
	else:
		return fibo(n-1) + fibo(n-2)
```

![스크린샷 2024-12-30 오후 4 12 04](https://github.com/user-attachments/assets/a9b3de20-c9d7-413a-acf2-8d931d32d102)

- 매번 함수가 호출될 때 마다 두 번씩 또 호출하기되기 때문에 트리의 높이를 k라고 한다면 k만큼 수행하는데  k는 n보다 적기 때문에 O(2^n)이라고 할 수 있다. O(n^3)보다 적인 데이터일 때도 처리시간이 많이 걸림

### O(m^n): exponential time

- O(2^n)과 거의 유사

### O(log n)

- 해당 시간 복잡도의 대표적인 예시는 ‘이진 검색’
    - 정렬 필수
- 한 번 처리가 진행될 때마다 검색해야하는 데이터의 수가 절반씩 줄어드는 알고리즘!

```python
def binary_search(target, data):
	# 데이터 정렬 필수
	data.sort() 
	start = 0 # 맨처음 위치
	end = len(data) - 1 # 맨 마지막 위치
	
	while start <= end:
		mid = (start+end) // 2 # 중간값
		
		if data[mid] == target:
			return mid
		elif data[mid] > target:
			end = mid - 1
		else:
			start = mid + 1
	return
```

![스크린샷 2024-12-30 오후 4 19 00](https://github.com/user-attachments/assets/35cbb7ab-14f5-422c-9454-a9857aa0c84e)

### Big O 표기법에서 중요한 점

- 상수 요소는 과감하게 버리기

### 피보나치 수열 최적화

- 피보나치 수열은 동일한 결과값을 한 번 더 수행하므로 트리구조가 k만큼 높이를 가진다.
- 만약 동일한 값이 있을 경우 수행하지 않는다면 어떻게 될까?

```python
from functools import lru_cache

@lru_cache
def fibo(n):
	if n == 0:
		return 0
	elif n == 1 or n == 2:
		return 1
	else:
		return fibo(n - 1) + fibo(n - 2)
```

- lru_cache를 이용하면 메모이제이션(Memoization)을 통해 중복된 값을 계산을 하지 않기 때문에 O(n) 시간 복잡도를 가짐
    - n번만큼 확인하기 때문