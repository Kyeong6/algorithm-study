"""
금광

n x m 크기의 금광 존재. 금광은 1 x 1 크기의 칸으로 나누어져 있으며, 각 칸은 특정한 크기의 금이 들어있음
채굴자는 첫 번째 열부터 출발하여 금을 캐기 시작.
맨 처음에는 첫 번째 열의 어느 행에서든 출발할 수 있음. 이후에 m-1번에 걸쳐서 매번 오른쪽 위, 오른쪽, 오른쪽 아래 3가지 중 하나의 위치로 이동
결과적으로 채굴자가 얻을 수 있는 금의 최대 크기를 출력하는 프로그램 작성

- 입력 조건
1. 첫째 줄에 테스크 케이스 T가 입력(1 <= T <= 1000)
2. 매 테스트 케이스 첫째 줄에 n과 m이 공백으로 구분되어 입력(1 <= n, m <= 20)
3. 둘째 줄에 n x m개의 위치에 매장된 금의 개수가 공백으로 구분되어 입력(1 <= 각 위치에 매장된 금의 개수 <= 100)


- 출력 조건
테스트 케이스마다 채굴자가 얻을 수 있는 금의 최대 크기 출력. 각 테스트 케이스는 줄바꿈을 이용해 구분
"""

# 테스트 케이스 입력
for tc in range(int(input())):
    n, m = map(int, input().split())
    array = list(map(int, input().split()))
    # DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index:index+m])
        index += m
    # DP 진행
    for j in range(1, m):
        for i in range(n):
            # 왼쪽 위에서 오는 경우
            if i == 0: left_up = 0
            else: left_up = dp[i-1][j-1]
            # 왼쪽 아래에서 오는 경우
            if i == n-1: left_down = 0
            else: left_down = dp[i+1][j-1]
            # 왼쪽에서 오는 경우
            left = dp[i][j-1]
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    
    result = 0
    for i in range(n):
        result = max(result, dp[i][m-1])
    
    print(result)