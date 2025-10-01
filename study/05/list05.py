"""
행렬의 곱셈:
2차원 행렬 arr1과 arr2를 입력받아 arr1에 arr2를 곱한 결과를 반환하는 solution 함수

제약조건:
1. 행렬 arr1, arr2의 행과 열의 길이는 2 ~ 100
2. 행렬 arr1, arr2의 데이터는 -10 ~ 20
3. 곱할 수 있는 배열 주어짐

분석:
- 행/열 길이가 2 ~ 100이므로 시간 복잡도 고려 x
- 행렬 크기 파악 후 변수 지정: (r1 * c2)
"""

def soultion(arr1, arr2):
    # 행렬 arr1과 arr2의 행과 열의 수
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    # 결과 저장: 행렬 계산 구조 생각
    ret = [[0] * c2 for _ in range(r1)]

    # 시간복잡도: O(N^3)
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                ret[i][j] += arr1[i][k] * arr2[k][j]
    
    return ret


arr1 = [[1,4],[3,2],[4,1]]
arr2 = [[3,3],[3,3]]

# [[15,15],[15,15],[15,15]]