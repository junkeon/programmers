def solution(arr1, arr2):
    answer = [[sum(a*b for a, b in zip(row1, row2)) for row2 in zip(*arr2)] for row1 in arr1]
    return answer
