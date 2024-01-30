# k번째 약수

# 자연수 n,k 설정
n, k = map(int, input().split())

# 약수를 담을 list
lst = list()

# 약수 확인
for i in range(1, n+1):
    div = n % i
    if (div == 0):
        lst.append(i)

# n의 약수의 개수가 k보다 작은 경우 확인
if len(lst) < k:
    print("-1")
else:
    print(lst[k-1])

# -------------------------------

# 다른 풀이

n, k = map(int, input().split())
# 개수 세기
cnt = 0
for i in range(1, n+1):
    if n % i == 0:
        # 약수 발견시 +1
        cnt += 1
    if cnt == k:
        print(i)
        break
# for-else문
else:
    print(-1)
    

        