## 037. 비밀지도

## 풀이

각 stage마다 클리어하지 플레이어 수와 스테이지에 도달한 플레이어 수를 구한 뒤 sort해준다.

## 생각

두번째 카카오 문제였다.
문제 자체는 간단하였으나, 처음에 어떻게 접근해야 할지 감을 잡기 힘들었다.

맨 처음 시도에서는 스테이지에 있는 수를 for으로 돌려서 계산을 하였으나 시간이 너무 걸렸다.
두번째는 count를 이용하여 스테이지를 for문으로 돌렸다.

데이터 구조는 가장 관리가 편한 딕셔너리를 사용하였다.

## 다른 사람 풀이

아이디어는 나와 같으나 for문 한번으로 해결한 것이 있어서 가져왔다.

```
def solution(N, stages):
    result = {}
    denominator = len(stages)
    for stage in range(1, N+1):
        if denominator != 0:
            count = stages.count(stage)
            result[stage] = count / denominator
            denominator -= count
        else:
            result[stage] = 0
    return sorted(result, key=lambda x : result[x], reverse=True)
```