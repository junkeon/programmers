def solution(m, n, board):
    answer = 0
    while True:
        remove_list = []

        for i in range(1, m):
            for j in range(1, n):
                char = board[i][j]
                if char == 'X':
                    continue
                if all(c == char for c in [board[i-1][j-1], board[i-1][j], board[i][j-1]]):
                    remove_list.extend([(i-1, j-1), (i-1, j), (i, j-1), (i, j)])

        remove_list = list(set(remove_list))
        answer += len(remove_list)

        if len(remove_list) == 0:
            return answer

        for j in range(n):
            stack = []
            for i in range(m):
                if (i, j) not in remove_list:
                    stack.append(board[i][j])

            N = m - len(stack)
            for i in range(m):
                if i < N:
                    board[i] = board[i][:j] + 'X' + board[i][j+1:]
                else:
                    board[i] = board[i][:j] + stack[i - N] + board[i][j+1:]
