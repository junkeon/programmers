def solution(land):
    score = land[0][:]
    
    for row in land[1:]:
        tmp = row[:]
        for i in range(4):
            tmp[i] += max(score[:i] + score[i+1:])
        score = tmp[:]

    return max(score)
