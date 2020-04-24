def solution(n):
    a1, a2 = 0, 1
    
    for _ in range(n-1):
        a1, a2 = a2, a1 + a2

    return a2 % 1234567
