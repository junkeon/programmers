def solution(skill, skill_trees):
    answer = len(skill_trees)
    
    for tree in skill_trees:
        s_idx = 0

        for s in [c for c in tree if c in skill]:                
            if s == skill[s_idx]:
                s_idx += 1
                
            else:
                answer -= 1
                break
            
    return answer