def solution(s):    
    return ' '.join([''.join([c.lower() if i%2 else c.upper() for i, c in enumerate(word)]) for word in s.split(' ')])