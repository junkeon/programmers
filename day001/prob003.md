## 003. 크레인 인형뽑기 게임

## 풀이

문제에 주어진 조건대로 움직여 결과를 구했다.

## 생각

제한사항에서 board의 배열의 최대크기가 30으로 주어졌기 때문에 문제의 조건대로 움직이면 별 문제가 없을 것 같았다.
특히 나는 board의 값을 변경하지 않고, 각 줄의 현재 위치를 고려할 pos라는 변수를 만들었다.
이 과정에서 다음과 같은 문제를 제대로 고려하지 못하였다.

첫번째는 pos라는 변수를 제대로 고려하지 못해 한참을 헤메었다.
특히 board의 index가 가장 윗줄이 0이고, 가장 아랫줄이 N-1임을 고려하지 못하였다.
마지막에는 board가 꽉찬 상태를 고려하지 않아서 첫번째 문제를 제외한 모든 문제에 런타임 에러가 떴다.

두번째는 빈 board를 접근하려는 move가 있음을 인지하지 못하여 헤메었다.
moves에 보면 비어 있는 칸을 접근하는 경우가 있는데, 이 경우 처리를 못해주어 에러가 발생하였다.

## 다른 사람 풀이

다른 사람들은 나의 풀이와는 다르게 move로 접근시 board의 값을 0으로 바꾸는 트릭을 이용하였다.
그런데 생각해보면, 매 move마다 0이 아닌 값을 탐색해야 하므로 시간이 더 걸릴 듯 하다.

```
def solution(board, moves):
    board = np.array(board).transpose()
    answer = [-1]
    count = 0
    for move in moves:
        print(move)

        for i, num in enumerate(board[move-1]):
            if num == 0:
                continue
            else:
                board[move-1][i] = 0
                if num == answer[-1]:
                    answer.pop()
                    count += 2
                    break
                answer.append(num)
                break

    return count
```
