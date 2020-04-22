def solution(n):
    n_one = bin(n).count('1')
    
    answer = n+1
    while True:
        if bin(answer).count('1') == n_one:
            return answer
        answer += 1
