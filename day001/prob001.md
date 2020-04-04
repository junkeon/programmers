## 001. 완주하지 못한 선수

## 풀이

participant와 completion을 각각 정렬한 후 비교하여 매치하지 않거나 남은 선수 이름을 반환

## 생각

처음에는 set으로 접근해서 풀려고 했다. 
그러나 set의 경우 중복된 원소에 대한 정보가 사라진다는 문제가 발생하였다. 
그래서 for문으로 participant를 돌면서 completion에 이름이 있으면 제거하고, 없으면 return하는 코드를 작성하였다.
이 경우에는 정확성 테스트를 통과하나, 효율성 테스트에서는 모두 실패하였다.
원소가 있는지 확인하는 과정에서 O(N)이 걸리고 또 제거하는 과정에서 O(N)이 걸려서 최종적으로 O(N^2)가 되어서 시간 초과가 발생하는 듯하다.
여러가지 접근 방법을 생각하다가, 정렬 후 비교하는 방식을 선택하여 문제를 해결하였다.

## 다른 사람 풀이

대부분의 사람들이 정렬 후 비교하는 방식으로 풀었다.
일부는 hash(혹은 dict)를 이용하거나 set으로 비교 후 없으면 내부적으로 비교하는 방식을 사용하는 듯하다.

가장 많은 댓글이 달린 혹은 많은 사람이 따라해 본 코드는 다음과 같다.

```
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    return list(answer.keys())[0]
```
