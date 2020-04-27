def solution(n,a,b):
    l = 0
    while n > 1:
        n //= 2
        l += 1
        
    s_a = str(bin(a-1)[2:]).zfill(l)
    s_b = str(bin(b-1)[2:]).zfill(l)
    
    for i in range(l):
        if s_a[i] != s_b[i]:
            return l-i
