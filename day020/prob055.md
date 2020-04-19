## 055. 더 맵게

## 풀이

heap queue를 이용하여 가장 덜 두 매운 음식의 스코빌 지수를 받아 계산하고 다시 queue에 넣는다. 그 과정에서 가장 덜 매운 음식의 지수가 K보다 크면 횟수를 리턴한다. 만약 스코빌 지수 수가 부족하였을 때 queue 안의 모든 스코빌 지수가 K보다 크면 0을 아니면 -1을 리턴한다.

## 생각

문제 자체는 매우 간단했지만, 생각보다 어려웠던 것이 효율성 테스트였다.

heap queue를 사용하지 않으면 매번 넣어줄때나 뺄때 정렬이 들어가기 때문에 음식의 수가 좀만 커지면 시간이 엄청 많이 소요하게 된다.
그렇기 때문에 효율적으로 정렬하는 방법이 필요했고 heap queue를 이용하게 되었다.

정확하게 말해서 이전에 풀때 heap queue를 알게 되어 이번 문제를 풀 때 큰 도움을 받았다.

heap queue를 자료구조 시간에서 배웠지만 어디에 사용하는지 알지 못했다.
그러나 이러한 문제를 풀면서 정말 중요하다는 것을 다시 한 번 깨닫게 되었따.

## 다른 사람 풀이
나와는 아이디어가 같지만 while문의 사용이 다른 풀이
```
import heapq as hq

def solution(scoville, K):

    hq.heapify(scoville)
    answer = 0
    while True:
        first = hq.heappop(scoville)
        if first >= K:
            break
        if len(scoville) == 0:
            return -1
        second = hq.heappop(scoville)
        hq.heappush(scoville, first + second*2)
        answer += 1  

    return answer
```
