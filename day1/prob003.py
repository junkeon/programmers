def solution(board, moves):
    answer = 0
    N = len(board)
    
    pos = [N-1 for _ in range(N)]
    
    for i in range(N):
        while pos[i] != 0 and board[pos[i]-1][i] > 0:            
            pos[i] -= 1
    
    stack = []
    for move in moves:
        if pos[move-1] == N:
            continue
        num = board[pos[move-1]][move-1]
        pos[move-1] += 1
        
        if len(stack) > 0 and stack[-1] == num:
            stack.pop()
            answer += 2
        else:
            stack.append(num)
    
    return answer