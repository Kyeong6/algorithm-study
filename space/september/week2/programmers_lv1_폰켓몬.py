"""
처음에 조합을 생각: 1 ~ 200,000이므로 N이 클수록 기하급수적으로 시간복잡도 커짐
문제를 자세히 읽어보면 해당 규칙 파악 가능
"""
def solution(nums):
    
    result = min(len(set(nums)), (len(nums)//2))
    
    return result

nums = [3,1,2,3]
print(solution(nums))