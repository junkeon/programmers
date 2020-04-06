def solution(n):
    
    answer, num = 0, 1
    
    for num in range(1, int(n**.5)+1):
        if n % num == 0:
            answer += num
            answer += n//num
            
    if num**2 == n:
        answer -= num

    return answer