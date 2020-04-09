def solution(arr1, arr2):    
    return [[num1 + num2 for num1, num2 in zip(row1, row2)] for row1, row2 in zip(arr1, arr2)]