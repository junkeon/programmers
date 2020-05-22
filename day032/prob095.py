def solution(N):
    a1, a2 = 0, 1
    
    for i in range(N):
        a1, a2 = a2, a1+a2
    
    answer = 2*(a1+a2)
    
    return answer
