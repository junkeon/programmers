## 005. K번째수

## 풀이

array를 commands의 값으로 slice한 후 정렬하여 k번째 수를 구한다.

## 생각

파이썬의 리스트 함수가 매우 잘되어 있고, 정렬도 간편하기 때문에 매우 쉬운 문제라고 생각한다.
다만 commands의 값이 인덱스 값이 아닌 순번을 나타내기 때문에 유의해야 했다.

## 다른 사람 풀이

lambda를 이용한 map 함수와 list comprehension을 이용한 풀이이다.

```
def solution(array, commands):
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))
```
