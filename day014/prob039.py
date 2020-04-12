def solution(dartResult):
    score = []
    c_score = 0
    i = 0
    
    while i < len(dartResult):
        if dartResult[i] in '023456789':
            c_score = int(dartResult[i])
            i += 1
        elif dartResult[i] == '1':
            if dartResult[i+1] == '0':
                c_score = 10
                i += 2
            else:
                c_score = 1
                i += 1

        elif dartResult[i] == 'S':            
            score.append(c_score)
            i += 1
        elif dartResult[i] == 'D':
            c_score = c_score ** 2
            score.append(c_score)
            i += 1
        elif dartResult[i] == 'T':
            c_score = c_score **3
            score.append(c_score)
            i += 1
            
        elif dartResult[i] == '*':
            if len(score) > 1:
                score[-2] *= 2
            score[-1] *= 2            
            i += 1
        elif dartResult[i] == '#':            
            score[-1] *= -1
            i += 1
            
    return sum(score)