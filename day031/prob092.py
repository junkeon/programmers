def solution(n, computers):    
    answer = 0
    
    queue = []
    search = list(range(n))
    
    while search:
        answer += 1
        i = search.pop()
        queue.append((i, computers[i]))
        while queue:
            i, com = queue.pop()
            for j, num in enumerate(com):
                if i == j:
                    continue
                if num == 1:
                    if j in search:
                        queue.append((j, computers[j]))
                        search.remove(j)
    
    return answer
