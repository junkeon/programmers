## 034. x만큼 간격이 있는 n개의 숫자

## 풀이

list comprehension

## 생각

처음에는 range를 이용한 풀이를 시도하였다.
그러나 range를 사용하면 x가 음수일때나 0일때 오류가 났다.
특히 0일 때는 range의 입력값이 모두 0이 되어 버리는데, 이러면 range에서 에러가 난다.
따라서 range가 아닌 list comprehension을 이용하는 것이 더 편하다.

## 다른 사람 풀이

pass