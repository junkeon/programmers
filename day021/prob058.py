def solution(clothes):
    c_dict = {}
    
    for c, t in clothes:
        if t not in c_dict:
            c_dict[t] = [c]
        else:
            c_dict[t].append(c)
                
    add = 1
    for v in c_dict.values():
        add *= (1 + len(v))
    
    return add - 1