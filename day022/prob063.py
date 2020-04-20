import heapq
def solution(stock, dates, supplies, k):
    L = len(dates)
    
    pq = []
    idx = 0
    answer = 0
    while stock < k:
        for i in range(idx, L):
            if dates[i] > stock:
                break
            heapq.heappush(pq, supplies[i] * -1)
            idx += 1
            
        stock += heapq.heappop(pq) * -1
        answer += 1
    
    return answer
