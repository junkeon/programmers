def convert(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]

def solution(n, t, m, p):
    return ''.join(map(lambda x:convert(x, n), range(t*m)))[p-1:m*t+p-1:m]
