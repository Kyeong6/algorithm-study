# k번째 수

# 테스트 케이스 t, 숫자 개수 n, 범위 s~e, 정렬 후 k번째 수

t = int(input())

# 테스트 케이스 개수만큼 반복
for i in range(1, t+1):
    n,s,e,k = map(int, input().split())
    elem = list(map(int, input().split()))
    elem = elem[s-1:e]
    elem.sort()
    print("#{} {}".format(i,elem[k-1]))