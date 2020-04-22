## 068. 땅따먹기

## 풀이

DP를 이용하여 현재 칸을 제외한 나머지의 칸들의 최고점들 중 최고를 뽑아 현재 위치에 더해준다.

## 생각

같은 칸을 밟을 수 없기에 현재 칸을 제외한 칸들로부터 올 수 있다.

따라서 현재 칸의 점수에 이전 최고점들 중 현재 칸을 제외한 최고점을 더한 값을 memoization하여 구해주면 된다.


## 다른 사람 풀이
나의 풀이와 다르게 별도의 메모리를 사용하지 않고, 입력 받은 메트릭스에서 해결한 풀이.
```
def solution(land):

    for i in range(1, len(land)):
        for j in range(len(land[0])):
            land[i][j] = max(land[i -1][: j] + land[i - 1][j + 1:]) + land[i][j]

    return max(land[-1])
```
