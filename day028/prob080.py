def solution(n, words):
    
    prev = ''
    for i, word in enumerate(words):
        if prev and prev[-1] != word[0] or word in words[:i]:
            a, b = divmod(i, n)
            return [b+1, a+1]
        prev = word
        
    return [0, 0]
