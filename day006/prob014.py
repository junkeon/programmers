def solution(s):
    answer = ''.join(sorted([c for c in s if c.islower()], reverse=True) + sorted([c for c in s if c.isupper()], reverse=True))
    return answer