def solution(progresses, speeds):
    days = []

    for p, s in zip(progresses, speeds):
        next_day = -(-(100-p)//s)

        if len(days) and days[-1][0] >= next_day:
            days[-1][1] += 1
        else:
            days.append([next_day, 1])
            
    _, answer = zip(*days)
    
    return list(answer)