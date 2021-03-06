## 028. 최대공약수와 최소공배수

## 풀이

누.가.봐.도. 유클리드 호제법!

## 생각

두 수의 최대공약수와 최소공약수, 역시 유클리드 호제법이다.
예전에 이 문제를 본 적이 있다.
그 때는 유클리드 호제법을 생각하지 못하고 for문부터 돌렸다.
그리고 그때 효율성에서 떨어졌던 것으로 기억한다.

하지만 이제는 안다.
유클리드 호제법이 짱이라는 걸.
괜히 수학을 배운 게 아니라는 걸.

## 다른 사람 풀이

이 풀이는 역시 유클리드 호제법이긴 하지만 lambda 기반 제귀법을 구현한것이다.
멋있다...

```
def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]
```