def solution(n, lost, reserve):
    answer = n
    
    for num in lost[:]:
        if num in reserve:
            lost.remove(num)
            reserve.remove(num)
            
    for num in lost[:]:
        for new_num in [num-1, num+1]:
            if new_num in reserve:
                lost.remove(num)
                reserve.remove(new_num)
                break
    
    answer -= len(lost)
    
    return answer