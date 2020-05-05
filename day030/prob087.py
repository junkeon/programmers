import string
u_case = string.ascii_uppercase

def solution(msg):
    answer = []
    a_dict = {c:i for i, c in enumerate(u_case, 1)}

    idx = 0

    while idx < len(msg):
        l = 1
        while idx+l <= len(msg) and msg[idx:idx+l] in a_dict:
            l += 1
        l -= 1
        
        answer.append(a_dict[msg[idx:idx+l]])
        a_dict[msg[idx:idx+l+1]] = len(a_dict) + 1
        
        idx += l
    
    return answer
