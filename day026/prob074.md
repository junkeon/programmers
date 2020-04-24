## 074. 행렬의 곱셈

## 풀이

zip을 사용하여 arr2를 transpose한 뒤, element product후 sum하여 행렬의 곱셈을 구한다.

## 생각

index를 통한 행렬의 곱셈은 시간이 많이 든다.

하지만 arr2를 transpose하고 element로 product를 한 후 더해주면 시간이 절약된다.

따라서 list comprehension을 이용하여 arr2를 zip하여 transpose한 후 element wise로 곱해주고 더해주면 행렬 곱셈이 된다.


## 다른 사람 풀이
나의 풀이에 큰 도움을 준 풀이
```
def productMatrix(A, B):
    return [[sum(a*b for a, b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

```
