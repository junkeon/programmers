def solution(cacheSize, cities):
    tic = 0    
    queue = []    
    for city in cities:
        city = city.lower()

        if city in queue:
            queue.remove(city)            
            tic += 1            
        else:
            if len(queue) >= cacheSize > 0:
                queue.pop(0)
            tic += 5

        if cacheSize != 0:
            queue.append(city)
            
    return tic
