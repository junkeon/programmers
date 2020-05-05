## 087. 압축

## 풀이

대문자로 이루어진 딕셔너리를 구축한 후 딕셔너리에 없을 때까지 현재 문자열의 길이를 늘린 후 사전에 추가한다.

## 생각

문제 조건에 맞춰 코드를 작성하였다.

나의 풀이의 경우 기존의 문자열을 조작하고 싶지 않아 인덱스로 접근을 하였는데, 인덱스로 접근하다보니 헷갈리는 부분이 많아 헤메었다.

## 다른 사람 풀이
문자열을 잘라서 풀어 더욱 깔끔한 풀이인거 같다.
```
def solution(msg):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    d = {k:v for (k,v) in zip(alphabet, list(range(1,27)))}
    answer = []

    while True:
        if msg in d:
            answer.append(d[msg])
            break
        for i in range(1, len(msg)+1):
            if msg[0:i] not in d:
                answer.append(d[msg[0:i-1]])
                d[msg[0:i]] = len(d)+1
                msg = msg[i-1:]
                break

    return answer
```
