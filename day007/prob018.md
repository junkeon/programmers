## 018. 문자열을 정수로 바꾸기

## 풀이

int 함수를 이용하여 정수로 바꿔준다.

## 생각

이 문제의 출제 의도는 알겠으나, 나는 바퀴를 다시 발명하지 않기 때문에 넘어간다.

## 다른 사람 풀이

아마 문제 출제 의도는 다음과 같이 푸는 것을 의도하지 않았나 싶다.
근데 여기도 int 함수는 쓰는걸...?

```
def strToInt(str):
    result = 0

    for idx, number in enumerate(str[::-1]):
        if number == '-':
            result *= -1
        else:
            result += int(number) * (10 ** idx)

    return result
```