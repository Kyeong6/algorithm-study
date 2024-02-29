# 랜선자르기(결정알고리즘)

def count(len):
    cnt = 0
    for x in line:
        cnt += (x//len)
    return cnt

k,n = map(int, input().split())

line = []
res = 0
largest = 0

for i in range(k):
    tmp = int(input())
    line.append(tmp)
    largest = max(largest, tmp)

lt = 1
rt = largest
while lt <= rt:
    mid = (lt+rt)//2
    if count(mid) >= n:
        res = mid
        lt = mid + 1
    else:
        rt = mid - 1

print(res)
