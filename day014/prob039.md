## 039. 다트 게임

## 풀이

각 문제에 맞는 조건문을 만들어 스테이지에 해당하는 점수를 계산하고 덧셈하여 점수를 구한다.

## 생각

문제가 복잡하게 느껴졌다.
단순한 코드로 계산할 수 없다고 생각했다.
그래서 조건문으로 조건을 나누어 계산했다.
굳이 정규표현식을 쓰고 싶지 않았다.
그랬더니 꽤나 더러운 코드가 완성되었다.
그래도 나는 마음에 든다.

## 다른 사람 풀이

정규표현식

```
import re


def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer
```