def solution(n):
    answer = 1
    num = 2
    s = 1
    
    while True:
        s += num
        if s > n:
            break
            
        if (n - s) % num == 0:
            answer += 1            
            
        num += 1
    return answer
