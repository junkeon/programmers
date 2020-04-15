def solution(w,h):
    total = w*h
    
    a, b = max(w, h), min(w, h)

    while b != 0:
        a, b = b, a%b
        
    gcd = a
    
    w, h = w//gcd, h//gcd
    
    return total - gcd * (w + h - 1)