## 043. 주식가격

## 풀이

문제 조건에 맞게 시뮬레이션하여 시간을 구한다.

## 생각

문제를 보면 한 틱에 세가지 일이 일어난다.

1. 다리를 다 지난 트럭은 큐에서 제거한다.
2. 무게 제한을 견디는 트럭이 있으면 추가한다.
3. 트럭이 앞으로 간다.

이 세가지 사건을 while문을 이용하여 시뮬레이션을 진행하였다.

그런데 당연한거지만, 신기하게도 세가지 사건의 순서에 따라 답이 달라졌다.
문제에서는 위의 세가지를 위와 같은 순서로 배치해야 정답처리가 되었다.

시뮬레이션하지 않고 알고리즘적으로 처리할 수 있는 방법이 있을 거 같기는 하다.
그래서 다른 사람들 풀이를 봤는데, 나와 비슷하게 매 틱마다 처리를 하는 방식으로 풀었다.
음...

## 다른 사람 풀이

내 풀이와는 다르게 남아 있는 시간을 계속해서 업뎃하지 않고, 현재 시간과 들어간 시간을 비교한 코드였다.
이런 방식이면 내 풀이보다 빠르지 않을까 싶다.
적어도 연산량이 줄 수 있는 거 같다.

돌려봤는데, 엄청 빠르다... 그래서 고침...

```
def solution(bridge_length, weight, truck_weights):
    time, total_weight = 0, 0
    q = []
    while truck_weights or q:
        time += 1

        if q and time - q[0][0] == bridge_length:
            t, w = q.pop(0)
            total_weight -= w

        if truck_weights and total_weight + truck_weights[0] <= weight:
            curr = truck_weights.pop(0)
            q.append((time, curr))
            total_weight += curr 

    return time
```
