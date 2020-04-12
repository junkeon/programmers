## 035. 직사각형 별찍기

## 풀이

list comprehension

## 생각

문자열 곱셈과 list comprehension

## 다른 사람 풀이

```
n, m = [int(x) for x in input().split()[:2]]
print('\n'.join(['*' * n] * m))
```