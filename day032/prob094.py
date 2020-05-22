def solution(begin, target, words):
    queue = [(begin, 0)]
    
    while queue:
        word, num = queue.pop(0)
        
        for candi in words[:]:
            if sum([alpha1 != alpha2 for alpha1, alpha2 in zip(word, candi)]) == 1:
                if candi == target:
                    return num + 1

                queue.append((candi, num+1))
                words.remove(candi)
    
    return 0
