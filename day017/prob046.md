## 046. 스킬트리

## 풀이

스킬 트리 중에서 스킬에 없는 것들은 빼고 스킬의 순서에 맞는지 인덱스를 써서 확인한 후 스킬 선행 순서에 맞지 않으면 전체 트리 수에서 빼주어 문제 조건에 맞는 트리의 수를 세준다.

## 생각

이 문제의 핵심은 스킬 선행 순서를 어떻게 확인할 것인지에 달려있다고 생각한다.
어떤 사람은 트리를 검사할 때 매번 스킬을 복사한 후 pop을 이용하여 검사를 했지만, 나는 시간 절약을 위해 인덱스를 이용했다.
사실 이 문제에서는 스킬의 수가 많지 않아 차이가 별로 없을 거 같지만 인덱스로 풀었다.

또한 나는 두번재 for 문 안에 스킬에 있는지 여부를 검사하는 대신 comprehension으로 미리 빼주어서 for문을 돌렸다.

## 다른 사람 풀이
pop을 이용한 풀이

```
def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

```
