import heapq
def solution(scoville, K):
    heapq.heapify(scoville)
    cnt = 0
    
    while len(scoville) > 1:
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        if first > K:
            return cnt
        heapq.heappush(scoville, first + 2 * second)
        cnt += 1
        
    if scoville and scoville[0] > K:
        return cnt
    return -1