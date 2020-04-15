def solution(arr):
    N = len(arr)
    answer = 0
    
    cnt = 0
    
    for i in range(N):
        if arr[i] == '(':
            cnt += 1
        else:
            cnt -= 1
            if arr[i-1] == '(':
                answer += cnt                
            else:
                answer += 1

    return answer