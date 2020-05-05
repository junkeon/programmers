def solution(files):
    new_list = []

    for file in files:
        idx = 0

        head = ''
        while not file[idx].isnumeric():
            head += file[idx]
            idx += 1

        number = ''
        while idx < len(file) and file[idx].isnumeric():
            number += file[idx]
            idx += 1

        new_list.append((head.lower(), int(number), file))
        
    new_list = sorted(new_list, key = lambda x : x[1])
    new_list = sorted(new_list, key = lambda x : x[0])
    
    *_, answer = list(zip(*new_list))
    return list(answer)
