def solution(n, arr1, arr2):
    answer = [format(num1|num2, f'{n}b').replace('1', '#').replace('0', ' ') for num1, num2 in zip(arr1, arr2)]
    return answer