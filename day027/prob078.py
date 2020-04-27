from itertools import combinations
def solution(nums):
    max_num = sum(sorted(nums)[-3:])
    primes = set(range(2, max_num+1))
    for i in range(2, int(max_num**.5)+1):
        primes -= set(range(i*2, max_num+1, i))
        
    return sum([1 for ns in combinations(nums, 3) if sum(ns) in primes])
