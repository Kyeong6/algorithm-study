# 이분검색

n,m = map(int, input().split())
a = list(map(int, input().split()))

# 오름차순 정렬(이분탐색 조건)
a.sort()

# 이분검색
lt = 0
rt = n-1

while (lt <= rt):
    # 이분탐색을 위한 중간인덱스
    mid = (lt+rt) // 2
    if a[mid] == m:
        print(mid+1)
        break
    elif a[mid] > m:
        rt = mid - 1
    else:
        lt = mid + 1