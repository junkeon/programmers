def solution(brown, red):
    brown += red
    for h in [h for h in range(3, int(brown**.5)+1) if brown%h == 0]:
        w = brown//h
        if (w-2)*(h-2) == red:
            return [w, h]
