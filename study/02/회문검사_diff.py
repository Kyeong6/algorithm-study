"""
Q. 회문은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열울 말한다.
만일 그 자체는 회문이 아니지만 한 문자를 삭제하여 회문으로 만들 수 있는 문자열이라면
우리는 이런 문자열을 유사회문이라고 부른다. 
만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 그 외는 2를 출력해야 한다.
Test Case: 
7
abba
summuus
xabba
xabbay
comcom
comwwmoc
comwwtmoc
"""
import sys
input = sys.stdin.readline

def is_palindrome(string, left, right, chance):
    while left < right:
        # 문자가 다를 경우
        if string[left] != string[right]:
            # 삭제 기회 존재
            if chance == 0:
                # 왼쪽 혹은 오른쪽 삭제하는 두 가지 경우 중 하나라도 존재하면 유사회문
                skip_left = is_palindrome(string, left+1, right, 1)
                skip_right = is_palindrome(string, left, right-1, 1)
                if skip_left == 0 or skip_right == 0:
                    return 1
                else:
                    return 2
            else:
                return 2
        left += 1
        right -= 1
    return 0
    
def palindrome(string):
    return is_palindrome(string, 0, len(string) - 1, 0)

n = int(input().strip())
words = [input().strip() for _ in range(n)]

for word in words:
    print(palindrome(word))


"""
방식: chance를 이용한 유사회문 조건(한 번만 제거) 및 재귀함수 사용
시간복잡도: O(n)
    - while문
"""