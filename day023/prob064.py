def solution(board):
    w, h = len(board), len(board[0])
    
    score = board[:]
    
    for i in range(1, w):
        for j in range(1, h):
            score[i][j] = (min(score[i-1][j-1], score[i-1][j], score[i][j-1]) + 1) * board[i][j]
            
    return max(map(max, score))**2
