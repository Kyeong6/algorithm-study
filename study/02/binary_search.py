finding_target = 14
finding_numbers = list(range(1, 17))

# 이진 탐색
def is_existing_target_number_binary(target, array):
    cur_min = 0
    cur_max = len(array) - 1
    cur_guess = (cur_min + cur_max) // 2
    find_count = 0

    # 같아질때까지 반복
    while cur_min <= cur_max:
        find_count += 1
        if array[cur_guess] == target:
            print(find_count)
            return True
        elif array[cur_guess] < target:
            cur_min = cur_guess + 1
        else:
            cur_max = cur_guess - 1

        # 위치 재설정
        cur_guess = (cur_min + cur_max) // 2
    
    return False

result = is_existing_target_number_binary(finding_target, finding_numbers)
print(result)