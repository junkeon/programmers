def solution(numbers, target):
    if numbers:
        return solution(numbers[1:], target - numbers[0]) + solution(numbers[1:], target + numbers[0])
    else:
        return 1 if target==0 else 0
