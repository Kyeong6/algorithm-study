"""
조기반환:
함수 끝까지 도달하기 전에 반환하는 기법
"""
def total_price(quantithy, price):
    total = quantithy * price
    if total > 100:
        return total * 0.9

    return total

"""
보호구문:
주요 로직 수행하기 전에 예외처리 추가하는 기법
"""
def calculate_average(numbers):
    if numbers is None:
        return None
    
    if not isinstance(numbers, list):
        return None
    
    if len(numbers) == 0:
        return None
    
    total = sum(numbers)
    avg = total / len(numbers)
    return avg

"""
합성함수:
2개 이상의 함수를 활용하여 함수를 추가로 만드는 기법
"""
def add_three(x):
    return x + 3

def square(x):
    return x * x

composed_function = lambda x: square(add_three(x))