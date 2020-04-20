## 063. 라면공장

## 풀이

현재 가진 양에서 버틸 수 있는 날까지 받을 수 있는 공급을 힙 큐에 넣고 가장 큰 공급을 받아 공급의 양을 최소화 한다.

## 생각

힙 큐를 사용하는 문제이다.

이 문제의 핵심은 최소한의 공급을 받기 위해서 언제 공급을 받는지를 선택해야 한다.

주어진 시간동안 하루에 소비하는 양은 정해져 있기 때문에 최소한의 공급은 최대 공급을 선택하는 것으로 볼 수 있다.
한 번에 가장 많은 공급을 받으면 그만큼 공급을 받는 횟수가 적어지기 때문이다.

그래서 다시 문제의 핵심은 어떻게 최대의 공급을 받을 것인가를 정해야 한다.
이를 위해서 힙 큐를 사용하게 된다. 
갖고 있는 밀가루의 양으로 버틸 수 있는 시간은 한정이 되어 있고, 그 사이에 공급을 받아야 한다.
따라서 갖고 있는 밀가루 양에서 공급을 받을 수 있는 양을 힙큐에 쌓아두고, 그 힙큐에서 가장 큰 것을 선택하면 된다.

이때 사용하는 것은 최대 힙 큐이고, 최소 힙 큐만을 지원하는 파이썬의 heapq로 구현하기 위해서는 -1을 곱해줘야 한다.


## 다른 사람 풀이
기본적으로 풀이의 아이디어가 다 비슷비슷하다.
```
import heapq

def solution(stock, dates, supplies, k):
    answer = 0
    idx = 0
    candidates = []
    supplies = [-x for x in supplies]
    while stock < k:
        # 현재 stock으로 버틸 수 있는 날 중에 추가로 밀가루 수령이 가능한 날과 그 날의 수량 저장
        for i in range(idx, len(dates)):
            if stock >= dates[i]:
                idx = i + 1
                heapq.heappush(candidates, supplies[i])  # 해당일의 공급 가능 물량을 candidates heap에 추가
            else:
                break

        # stock = stock + heapq._heappop_max(candidates)
        stock = stock + heapq.heappop(candidates) * -1
        answer = answer + 1

    return answer
```
