"""
방식: 순회하면서 해당 숫자가 이전에 판별한 소수와 나눌 수 있는지 확인하는 방식
시간복잡도: O(N^2)
    - Flag 변수를 이용한 이중반복문 사용
"""

def find_decimal(number):
    # 소수 리스트 생성
    decimal_list = list()

    for i in range(2, number+1):
        # Flag 변수: 소수 판별
        is_prime = True

        # 기존의 소수들로 나눠보면서 확인
        for decimal in decimal_list:
            # 하나라도 나눠지면 소수 x
            if i % decimal == 0:
                is_prime = False
                break
        
        if is_prime:
            decimal_list.append(i)
    
    return decimal_list

# num = 20
# print(find_decimal(num))


"""
* 모든 수 탐색이 아닌 이전에 찾은 소수들 이용
    - 이미 소수가 아닌 수들은 거르고 오기 때문에 불필요한 연산 줄임
방식: 소수의 제곱근 성질 이용
시간복잡도: O(N * rootN)
    - 두 번째 반복문에서 조건문을 통해 최대 root N만큼만 루프를 돌기 때문
"""
def develop_find_decimal(number):
    # 소수 리스트 생성
    decimal_list = list()

    # 소수는 2와 3의 조합으로 생성될 수 없는 수
    for i in range(2, number+1):
        # 이미 찾은 소수들로만 나누어 확인
        for decimal in decimal_list:
            if (i % decimal == 0) and decimal * decimal <= i:
                # 나누어 떨어지는 경우 소수가 아니므로 중단
                break
        else:
            decimal_list.append(i)
    
    return decimal_list

# num = 20
# print(develop_find_decimal(num))


"""
* 소수를 가장 빨리 찾는 방법
    - 검색을 통해 알게된 방식
방식: 에라토스테네스의 체
    - 배수 개념 이용: 2부터 시작하여 특정 숫자의 배수 제거
시간복잡도: O(N*log*logN)
    - 배수 제거될 때 한 번만 접근
    - 제곱근까지만 확인
"""
import math

def eratosthenes(number):
    # 입력된 숫자만큼의 소수 판별 리스트 생성 (True: 소수, False: 소수가 아님)
    decimal_list = [True] * (number+1)

    decimal_list[0], decimal_list[1] = False, False

    # 2부터 root N까지 반복
    for i in range(2, int(math.sqrt(number)) + 1):
        # 소수일 경우
        if decimal_list[i]:
            # i의 배수를 소수가 아닌 수 처리
            for j in range(i * i, number+1, i):
                decimal_list[j] = False
    
    # True인 값만 최종 리스트에 적재
    detected = [j for j in range(number+1) if decimal_list[j]]

    return detected

num = 20
print(eratosthenes(num))
