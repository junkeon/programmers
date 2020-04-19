from itertools import permutations

def solution(numbers):
    
    p_set = set()
    for n in range(1, len(numbers)+1):
        for n_s in permutations(numbers, n):
            p_set.add(int(''.join(n_s)))

    num = max(p_set)
    p_set -= {0, 1}
    for i in range(2, int(num**.5)+1):
        p_set -= set(range(2*i, num+1, i))
    
    return len(p_set)