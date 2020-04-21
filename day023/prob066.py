def solution(s):
    answer = []
    s = sorted(s[2:-2].split('},{'), key=lambda x:len(x))

    prev = set()
    for row in s:
        curr = set(row.split(','))
        answer.append(int(list(curr - prev)[0]))
        prev = curr

    return answer
