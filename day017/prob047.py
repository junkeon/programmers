def solution(priorities, location):
    prior_list = list(enumerate(priorities))
    stack = []

    while prior_list:
        i, p = prior_list.pop(0)

        return_list = []
        while stack and stack[-1][1] < p:
            return_list.append(stack.pop())

        if return_list:
            prior_list += return_list[::-1]

        stack.append((i, p))

    for i, (j, _) in enumerate(stack, 1):
        if j == location:
            return i