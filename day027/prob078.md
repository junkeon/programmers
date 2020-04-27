## 078. 소수 만들기

## 풀이

3개의 수로 만들 수 있는 최대 수까지의 소수 리스트를 구하고, combinations을 이용하여 가능한 모든 조합에 대해 덧셈을 한 후 리스트에 있는 수를 구한다.

## 생각

에라토스테네스의 체를 이용하여 소수 리스트를 구하고, combinations 함수로 가능한 모든 조합을 구하였다.

구한 모든 조합에 대해 소수 리스트에 있는지 확인하여 개수를 구해주었다.

## 다른 사람 풀이
비교적 깔끔하게 짠 코드가 있었따.
깔끔하게 짜긴 했으나, 소수 판별 과정에서 비효율이 발생할 것 같다.
에라토스테네스 체를 이용하거나 적어도 cand**.5+1까지만 for를 돌려도 좋을 거 같다.
```
def solution(nums):
    from itertools import combinations as cb
    answer = 0
    for a in cb(nums, 3):
        cand = sum(a)
        for j in range(2, cand):
            if cand%j==0:
                break
        else:
            answer += 1
    return answer
```
