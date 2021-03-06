## 070. 숫자의 표현

## 풀이

더하는 수의 개수를 1부터 늘려나가면서 가능한 것들의 가짓수를 센다.

## 생각

등차 수열의 합 공식을 이용한다.

예를 들어 a부터 시작하여 a+(b-1)까지 더하면 b x x + (b-1) x b/2가 된다.

따라서 만약 주어진 숫자 n이 b개의 숫자의 합으로 표현이 된다면, (n - (b-1)xb/2) / b = a가 된다.

이때 a는 자연수이므로 (n - (b-1)xb/2)는 b의 배수가 되어야 한다.

또한 a가 자연수 (n - (b-1)xb/2)는 0보다 커야 한다. 

이 두가지 조건을 맞춰 b를 1부터 늘려나가면서 탐색을 하면된다.

## 다른 사람 풀이
다음의 풀이가 된다는데 왜 되는지는 생각을 좀 해봐야겠다.
```
def expressions(num):
    return len([i  for i in range(1,num+1,2) if num % i is 0])
```
