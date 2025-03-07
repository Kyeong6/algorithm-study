"""
Q. 배달의 민족 서버 개발자로 입사했다.
상점에서 현재 가능한 메뉴가 ["떡볶이", "만두", "오뎅", "사이다", "콜라"] 일 때, 유저가 ["오뎅", "콜라", "만두"] 를 주문했다.
그렇다면, 현재 주문 가능한 상태인지 여부를 반환하시오.
Test Case: 
menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]

방식: 두 가지 방식 사용, 문제의 의도는 시간복잡도를 어떻게 줄일 수 있나?인 것 같다고 판단하여 시간 복잡도 개선 진행
    - basic: 완전탐색 이용 -> 중복을 고려하지 못해 오답처리될 확률 높음(추가적 Test case 파악의 중요성)
    - improve: 집합 이용 -> 해시 테이블을 사용하여 즉시 탐색 가능, 존재 유무를 파악할 때 유용
시간복잡도: 
    - basic: 이중 반복문을 이용한 완전탐색 진행하여 O(n^2)
    - improve: 집합변환 및 탐색 진행하여 O(n)
"""
def basic_is_ordered(menus, orders):
    cnt = 0
    correct = len(orders)

    # 완전탐색: O(n^2)
    for menu in menus:
        for order in orders:
            if menu == order:
                cnt += 1
    
    # 배달 가능 여부 판단
    if cnt == correct:
        return True
    else:
        return False

def improve_is_ordered(menus, orders):
    # 중복 제거: O(n)
    menu_set = set(menus)

    # 탐색: O(m)
    for order in orders:
        # 집합(set)은 해시 테이블을 사용하여 즉시 탐색 가능, 존재 유무를 파악할 때 유용
        if order not in menu_set:
            return False
    return True


menus = ["떡볶이", "만두", "오뎅", "사이다", "콜라"]
orders = ["오뎅", "콜라", "만두"]
print(basic_is_ordered(menus, orders))