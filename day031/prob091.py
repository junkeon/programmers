def solution(n):
    a1 = 0
    a2 = 1
    
    for i in range(n):
        a1, a2 = a2, a1 + a2
    
    return a2 % 1000000007
