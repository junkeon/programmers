## 088. 파일명 정렬

## 풀이

파일명에서 header, number, tail을 모두 분리한 후 먼저 number로 정렬하고, header로 정렬하여 파일명을 출력한다.

## 생각

맨처음에는 딕셔너리를 이용하여 계층 구조를 저장하고 정렬을 하였다.

하지만 이럴 경우 딕셔너리 안의 딕셔너리 구조가 생겨 접근이 귀찮았다.

하지만 다른 사람 풀이를 참고하여 딕셔너리 구조를 사용하지 않고, header와 number를 이용하여 number를 먼저 정렬하고 header를 정렬하였더니 더욱 깔끔한 코드가 탄생했다.

하지만 정규표현식을 사용하고 싶지 않아 일일이 header와 number을 분리하다 보니 코드가 좀 길어진 면이 있다.

## 다른 사람 풀이
정규 표현식과 정렬을 이용하여 3줄만에 끝낸 코드
정규 표현식을 따로 썼다는 점이 맘에 들지 않지만 놀라웠다.
```
import re

def solution(files):
    a = sorted(files, key=lambda file : int(re.findall('\d+', file)[0]))
    b = sorted(a, key=lambda file : re.split('\d+', file.lower())[0])
    return b
```
