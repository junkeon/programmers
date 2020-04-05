def solution(n):
    num_set = set(range(2, n+1))
        
    for i in range(2, int(n**.5)+1):
        num_set -= set(range(i*2, n+1, i))

    return len(num_set)