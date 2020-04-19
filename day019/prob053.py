def solution(p):
    if not p:
        return p
        
    u = ''
    check = True
    score = 0
    for i in range(len(p)):
        sym = p[i]
        score += 1 if sym == '(' else -1
        check = check and score >= 0
        u += sym
        
        if score == 0:
            break
            
    v = p[i+1:]
    
    if check:
        return u + solution(v)
    
    return '(' + solution(v) + ')' + u[1:-1].replace('(', 'a').replace(')', '(').replace('a', ')')