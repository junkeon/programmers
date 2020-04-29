## 083. 프렌즈4블록

## 풀이

먼저 전체 board를 스캔하여 지워지는 칸들의 위치를 저장한다. 만약 지워지는 칸이 없으면 여태 지워진 칸들의 수를 리턴한다. 이후 각 열에 대해 위에서부터 지워지지 않는 칸들의 정보를 순서대로 저장한 후 지워지고 난 후부터의 칸들부터 차례대로 채워나간다. 이를 지워지는 칸들이 없어질때까지 반복한다.

## 생각

문제 조건에 따라 지워지는 칸들은 현재 칸의 블록과 좌측, 상단 좌측, 상단의 블록이 모두 같은 칸들이다.

따라서 인덱스를 1부터 시작하여 이 조건에 맞는 칸들의 위치를 저장해주면 되는데, 이때 지워진 칸들은 제외해야 한다.

지워지는 칸들의 수를 모두 센 후에는 중복을 제거하고 지워지는 칸들의 개수를 누적하여 저장한다.

이후에는 실제로 칸들을 지워줘야 한다.

칸들이 지워진 후에는 블록이 아래로 내려오기 때문에, 위에서부터 지워지지 않는 칸들을 저장하고 위에서부터 지워지는 칸들의 수만큼 X표시하고 그 이후부터는 지워지지 않는 칸들의 정보를 덮어씌운다.

## 다른 사람 풀이
다른 사람들의 풀이 역시 기본적으로 스캔 후 지워주는 방식이다.
스캔 과정은 모두 동일하지만, 어떻게 지워줄까에서 많이 차이가 나는 듯하다.
나의 풀이의 경우 위에서부터 스캔해서 지워지지 않는 칸들을 저장해서 덮어씌우는데, 아래의 코드는 아래부터 시작해서 지워지지 않는 칸의 경우 아래로 내려서 지워주었다.
```
def solution(m, n, board):
    answer = 0
    board = [["-" for _ in range(n)]] + [list(b) for b in board]

    while True:
        pos_to_remove = [[False for _ in range(n)] for _ in range(m+1)]
        cnt = 0
        for r in range(1, m):
            for c in range(n-1):
                if board[r][c] != "-" and board[r][c] == board[r][c+1] == board[r+1][c] == board[r+1][c+1]:
                    for i in range(r, r+2):
                        for j in range(c, c+2):
                            pos_to_remove[i][j] = True

        for c in range(n):
            for r in range(1, m+1):
                if pos_to_remove[r][c]:
                    cnt += 1
                    for k in range(r, 0, -1):
                        board[k][c] = board[k-1][c]

        if cnt == 0:
            return answer
        answer += cnt
```
