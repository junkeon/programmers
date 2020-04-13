def solution(n):
    d = {0:'1', 1:'2', 2:'4'}

    answer = ''
    c = 0
    while n >= 3**c:
        n -= 3**c
        answer += d[n//3**c%3]
        c += 1

    return answer[::-1]

'''
def solution(n):
    d = ['1', '2', '4']

    answer = ''
    
    while n > 0:
        n -= 1
        answer += d[n%3]
        n //= 3
        
    return answer[::-1]
'''