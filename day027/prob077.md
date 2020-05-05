## 077. 짝지어 제거하기

## 풀이

각 문자에 대해 stack의 마지막 문자와 비교하여 같으면 마지막 문자를 빼고, 다르면 현재 문자를 stack의 마지막에 추가한다.

## 생각

효율성을 위해서는 stack을 이용하였다.

이어 붙이기 위해서는 마지막 문자만을 검사하게 되는데, 만약 검사를 하다 제거가 된다면 그 전의 문자가 마지막이 되어야 한다.

따라서 이 자료구조를 위해 stack을 사용하였고, 검사를 위해 마지막 문자만을 확인하면 되었다.

## 다른 사람 풀이
단순, 간결 패스!
```

```