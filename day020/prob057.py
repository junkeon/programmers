def solution(citations):
    citations.sort(reverse=True)
    
    for i, c in enumerate(citations,1):
        if c < i:
            return i-1
    return i