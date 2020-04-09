def solution(n, m):
    num1, num2 = max(n, m), min(n, m)
    
    while num2 != 0:
        num1, num2 = num2, num1%num2
        
    return [num1, n*m/num1]