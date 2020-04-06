import string

def solution(s, n):
    lower, upper = string.ascii_lowercase, string.ascii_uppercase
    
    answer = ''
    for c in s:
        if c in lower:
            answer += lower[(lower.index(c)+n)%26]
        elif c in upper:
            answer += upper[(upper.index(c)+n)%26]
        else:
            answer += c
            
    return answer