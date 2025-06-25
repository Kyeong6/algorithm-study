def calculate(array):
    # 연산 결과합
    plus_multiply_sum = 0

    # 리스트 내의 숫자 탐색: 
    for number in array:
        # 해당 숫자가 0,1이거나 합이 0,1일 경우 '+' 사용
        if number <= 1 or plus_multiply_sum <= 1:
            plus_multiply_sum = plus_multiply_sum + number
        else:
            plus_multiply_sum = plus_multiply_sum * number

    return plus_multiply_sum

lst = [0,3,5,6,1,2,4]
print(calculate(lst))