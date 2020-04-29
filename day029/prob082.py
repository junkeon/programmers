import string
lcase = string.ascii_lowercase

def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    str1 = [str1[i:i+2] for i in range(len(str1)-1) if all(p in lcase for p in str1[i:i+2])]
    str2 = [str2[i:i+2] for i in range(len(str2)-1) if all(p in lcase for p in str2[i:i+2])]
    
    i_key = set(str1) & set(str2)
    u_key = set(str1) | set(str2)
    
    inter = sum([min(str1.count(p), str2.count(p)) for p in i_key])
    union = sum([max(str1.count(p), str2.count(p)) for p in u_key])
    
    return int(inter / union * 65536 if union else 65536)
