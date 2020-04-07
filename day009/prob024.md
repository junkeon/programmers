## 024. 정수 내림차순으로 배치하기

## 풀이

주어진 수를 문자열로 변환한 후 내림차순으로 정렬한 후 정수로 바꾸어 리턴한다.

## 생각

22, 23번 문제와 똑같은 문제였다.
파이썬의 내장 함수들을 이용하면 간단하게 해결할 수 있었다.
파이썬 짱짱

## 다른 사람 풀이

퀵소트를 구현해서 정렬을 했다라... 흠...

```
def quicksort(x):
    if len(x) <= 1:
        return x

    pivot = x[len(x) // 2]
    less = []
    more = []
    equal = []
    for a in x:
        if a < pivot:
            less.append(a)
        elif a > pivot:
            more.append(a)
        else:
            equal.append(a)

    return   quicksort(more)+ equal +quicksort(less)

def solution(n):
    n = str(n)
    new = []
    for i in n :
        new.append(int(i))
    result = quicksort(new)

    answer = ''
    for i in result :
        answer += str(i)
    return int(answer)
```
