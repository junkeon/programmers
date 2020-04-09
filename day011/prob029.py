def solution(num):
    cnt = 0
    
    while num != 1:
        num = num%2 and 3*num+1 or num//2
        cnt += 1
                
    return cnt if cnt <= 500 else -1