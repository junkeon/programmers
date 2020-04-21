def solution(s):
    cnt = 0
    for sym in s:
        cnt += 1 if sym == '(' else -1
            
        if cnt < 0:
            return False
        
    return cnt == 0
