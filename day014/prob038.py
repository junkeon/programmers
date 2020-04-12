def solution(N, stages):
    
    stage_dict = {n:[stages.count(n), 0] for n in range(1, N+1)}
    last_num = stages.count(N+1)
    
    for num in range(N, 0, -1):
        stage_dict[num][1] = stage_dict[num][0] + last_num
        last_num = stage_dict[num][1]
        
    ans, _ = zip(*sorted(stage_dict.items(), key=lambda x:x[1][0]/(x[1][1]+1e-3), reverse=True))
    
    return list(ans)