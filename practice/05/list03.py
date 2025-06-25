"""
두 개 뽑아서 더하기:
정수 배열 numbers를 이용하여 numbers에서 서로 다른 인덱스에 있는 2개의 수를 뽑아 
더해 만들 수 있는 모든 수를 배열에 오름차순으로 담아 반환하는 solution() 함수 

제약조건:
1. numbers의 길이: 2 ~ 100
2. numbers의 모든 수 0 ~ 100

분석:
- 처음 생각했을 때는 이중반복문(O(N^2))을 이용하여 1,2번째 수를 더하여 새로운 배열에 담기
    - 제약조건에 따라 최대 데이터 개수: 100
- N=100 이므로 시간복잡도 영향 x
"""
def solution(numbers):

    # 제약조건 반영
    if len(numbers) < 2:
        return 

    result = []
    
    # O(N^2)
    for i in range(len(numbers)): 
        for j in range(i+1, len(numbers)):
            sum = numbers[i] + numbers[j]
            result.append(sum)
    
    # O(N^2): set()은 해시 알고리즘이지만, 데이터의 개수가 N^2
    # 정렬: O(N^2log(N^2)) -> 데이터의 개수 영향, 최종 시간복잡도
    result = list(set(sorted(result)))

    return result

# numbers = [2]  
numbers = [2,1,3,4,1]
print(solution(numbers))