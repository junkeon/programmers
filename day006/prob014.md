## 014. 문자열 다루기 기본

## 풀이

길이가 4 또는 6인지 판별함과 동시에 숫자인지를 확인하여 리턴하다.

## 생각

이번 풀이의 핵심은 논리 연산자를 복잡하게 사용하지 않고 푸는 것과 숫자인지를 판별하는 것에 있다고 생각한다.

첫번째로 길이가 4 또는 6인지를 판별하기 위해서는 기본적으로 or를 이용하여 두 개의 판별값을 묶어야 한다.
하지만 그렇게 되면 숫자인지도 같이 판별하기 위해서 괄호로 묶어주거나 and를 두번 사용하여 답을 리턴하게 된다.
따라서 이렇게 복잡하게 하기보다는 in과 리스트(혹은 튜플)을 이용하면 간편하게 판별할 수 있다.

두번째는 숫자인지를 판별하는 것이다.
다른 사람들의 풀이를 보면 예외처리와 int 함수를 이용하여 숫자인지를 판별하고자 하였다.
하지만 파이썬의 문자열에 기본적인 함수인 isdigit함수를 이용하면 예외처리를 사용하지 않고 결과를 알 수 있다.
예외처리를 사용하는 방법의 단점은 예외가 발생하였을 때 어디서 나온 에러인지에 따라 처리를 잘못하면 코드의 결과가 달라진다는 데에 있다.
따라서 우리가 목적하는 바에만 집중하기 위해 isdigit이라는 함수를 사용하면 편하다.
다만 이 함수가 존재하는지 알지 못하면 사용할 수 없다.

## 다른 사람 풀이

혹은 정규표현식을 사용하여 풀 수도 있다.
사실 너무 간단한 문제라 정규표현식으로 푸는 것이 비효율적일 수 있는데, 문제가 복잡해지면 오히려 정규표현식이 더 편리한 경우가 많다.

```
def alpha_string46(s):
    import re
    return bool(re.match("^(\d{4}|\d{6})$", s))
```