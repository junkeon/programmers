def solution(arr, divisor):
    answer = [num for num in arr if num%divisor==0]
    return sorted(answer) if len(answer) else [-1]