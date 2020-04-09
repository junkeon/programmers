## 033. 행렬의 덧셈

## 풀이

두 번의 list comprehension

## 생각

zip을 활용한 list comprehension을 이용하여 풀었다.
다른 사람 풀이 중 안의 list comprehension을 map으로 바꾼 사람이 있길레 그 풀이대로 했더니 시간이 증가했다.
좀 길어보이지만, 이 풀이가 가장 나은 듯 하다.

## 다른 사람 풀이

```
def sumMatrix(A,B):
    return [list(map(sum, zip(*x))) for x in zip(A, B)]
```