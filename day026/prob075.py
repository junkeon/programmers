def solution(s):
    return ' '.join([word[:1].upper()+word[1:].lower() for word in s.split(' ')])
