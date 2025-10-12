"""
정석은 Hash를 이용하는 것이지만, Pythonic 하게 풀기
- startswith() : 문자열에서 존재여부 파악하는 데 용이(boolean)
    - endswith() 사용 가능
"""

def solution(phone_book):
    
    # 정렬 진행: 어떤 번호가 다음 번호의 접두사라면 항상 바로 뒤에 위치
    phone_book.sort()
    
    # 인접한 번호끼리 비교
    for i in range(len(phone_book) - 1):
        # 현재 번호가 바로 다음 번호의 접두사인지 확인: 문자열 startwith() 사용 가능
        # 문자열A.startswith(문자열B) : 문자열 A가 문자열 B로 시작? (boolean)
        if phone_book[i+1].startswith(phone_book[i]):
            return False
            
    return True