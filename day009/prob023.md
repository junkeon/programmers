## 023. 자연수 뒤집어 배열로 만들기

## 풀이

주어진 수를 문자열로 변환한 후 그 역순에 대해 각 자리 수를 다시 int로 매핑하여 리턴한다.

## 생각

22번 문제와 거의 같은 방식으로 풀었다.
다만 더해주지 않고 리스트 형식으로 반환한다는 점과 역순을 넣었다는 점이 달랐다.
같은 방식으로 푼 사람들이 많았다.

## 다른 사람 풀이

```
def digit_reverse(n):
    tmp=str(n)[::-1]
    ret=[]
    for i in tmp:
        ret.append(int(i))
    return ret
```