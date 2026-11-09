def solution(numbers, target):
    length = len(numbers)
    answer = 0
    
    def dfs(result, idx):
        nonlocal answer
        if idx < length - 1:
            idx += 1
            dfs(result + numbers[idx], idx)
            dfs(result - numbers[idx], idx)
        else:
            if result == target:
                answer += 1
            
    dfs(numbers[0], 0)
    dfs(-numbers[0], 0)
    return answer