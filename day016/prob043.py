def solution(prices):
    answer = [0] * len(prices)
    stack = []
    for i in range(len(prices)-1):
        while stack and stack[-1][1] > prices[i]:
            j, _ = stack.pop()
            answer[j] = i - j
        stack.append((i, prices[i]))
            
    for i, _ in stack:
        answer[i] = len(prices) - i - 1
        
    return answer
