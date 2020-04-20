## 061. 타겟 넘버

## 풀이

가능한 모든 경우에 대해 연산 결과가 target인 수를 세어 리턴한다.

## 생각

가능한 모든 경우를 고려해주어야 한다.

처음에는 for문을 통한 방법으로 풀었다.

하지만 재귀로 푸는 방식이 있었다.

이 문제를 재귀로 풀때 간단한 이유는 연산의 횟수가 모두 같기 때문이며, 연산이 더하기나 빼기 둘 중 하나이기 때문이다.

따라서 재귀의 방법으로 각각에 대해 연산을 하여 결과를 받아오면 매우 간결하고 놀라운 코드로 풀 수 있게 된다.

## 다른 사람 풀이
현재 나의 풀이에 매우 큰 영향을 미친 답안.
하지만 현재 내 풀이가 더 간결하다.

```
def solution(numbers, target):
    if not numbers and target == 0 :
        return 1
    elif not numbers:
        return 0
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])
```
