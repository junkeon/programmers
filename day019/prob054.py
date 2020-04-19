def solution(numbers):
    numbs = map(str, numbers)
    return str(int(''.join(sorted(numbs, key=lambda x:x*3,reverse=True))))