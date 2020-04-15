def solution(heights):
    N = len(heights)
    
    heights = heights[::-1]
    answer = [0] * N
    stack = []
    
    for i in range(N):
        while stack and stack[-1][1] < heights[i]:
            j, _ = stack.pop()
            answer[j] = N - i
        stack.append((i, heights[i]))
        
    return answer[::-1]