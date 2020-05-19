def solution(n):
    answer = []
    
    for i in range(n):
        answer = answer + [0] + [1^bit for bit in answer[::-1]]
    
    return answer
