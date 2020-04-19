from itertools import permutations
def solution(baseball):
    n = 3    
    candi = list(map(lambda x:''.join(map(str, x)), permutations(range(1, 10), n)))
                    
    for num, s, b in baseball:
        num1 = str(num)        
        for num2 in candi[:]:
            _s, _b = 0, 0
            for i in range(n):
                _s += 1 if num1[i] == num2[i] else 0
                for j in range(n):
                    if i == j:
                        continue
                    _b += 1 if num1[j] == num2[i] else 0
                
            if _s!=s or _b!=b:                
                candi.remove(num2)
        
    return len(candi)