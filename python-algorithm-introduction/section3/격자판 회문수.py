# 격자판 회문수

a = [list(map(int, input().split())) for _ in range(7)]
cnt = 0

# i의 범위가 3인 이유 : 7개의 칸에서 5개의 회문 확인이므로 3개의 묶음을 확인하면 됨
# j는 행을 파악
for i in range(3):
    for j in range(7):
        # 행
        lst = a[j][i:i+5]
        if lst == lst[::-1]:
            cnt+=1
        # 열(슬라이싱 불가능)
        for k in range(2): # 5//2
            if a[i+k][j] != a[i+5-k-1][j]:
                break
        # for-else : for문이 정상적으로 끝날 경우
        else:
            cnt+=1

print(cnt)