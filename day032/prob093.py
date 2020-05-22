import heapq

def solution(n, costs):
    answer = 0
    
    cost_dict = {}
    for i, j, c in costs:
        cost_dict[(i, j)] = c
        cost_dict[(j, i)] = c
            
    rest = list(range(n))
    cost_h = []
    cost, idx = 0, 0
            
    while rest:
        while cost_h and True:
            cost, idx = heapq.heappop(cost_h)
            if idx in rest:
                break
                
        rest.remove(idx)
        answer += cost
        
        for j in rest:
            if (idx, j) in cost_dict:
                heapq.heappush(cost_h, (cost_dict[(idx, j)], j))
    
    return answer
