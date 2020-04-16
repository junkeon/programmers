def solution(s):
    L = len(s)    
    
    min_num = L
    
    for num in range(1, L//2+1):
        zip_s = ''
        cnt = 0
        target = ''
        for i in range(0, L, num):
            piece = s[i:i+num]
            if target == piece:
                cnt += 1
            else:
                if target:
                    zip_s += f'{cnt}{target}' if cnt > 1 else f'{target}'
                cnt = 1
                target = piece

        zip_s += f'{cnt}{target}' if cnt > 1 else f'{target}'
        
        min_num = min(min_num, len(zip_s))
        
    return min_num