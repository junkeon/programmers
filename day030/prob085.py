from itertools import combinations

def solution(relation):
    N = len(relation)
    L = len(relation[0])
    
    keys = []
    candi = list(range(L))
    
    for n in range(1, L+1):
        for c in combinations(candi, n):
            if any(all(k in c for k in key) for key in keys):
                continue
            if len(set(tuple(relation[i][j] for j in c) for i in range(N))) == N:
                keys.append(c)
                
    return len(keys)
