## 053. 괄호 변환 

## 풀이

(의 개수와 )의 개수를 비교하여 균형잡힌 괄호를 판별하고, )가 (보다 많아지는지를 확인하여 올바른 괄호 문자열을 판별한다.
그리고 문제에서 주어진 알고리즘대로 수행하여 결과를 리턴한다.

## 생각

문제는 매우 복잡하지만, 실제로는 문제에서 주어진 알고리즘대로만 수행하면 되는 문제였다.

다만 여기에서 균형잡힌 괄호 문자열과 올바른 괄호 문자열을 어떻게 판별할 것인가와 4-4번 과정 괄호의 방향을 어떻게 뒤집을 것인가만 해결하면 되었다.

균형잡힌 괄호 문자열을 판별하기 위해서 (와 )의 개수를 비교하였다.
(와 )의 개수가 같아지는 시점에서 그 이전의 괄호들이 균형잡힘을 알 수 있기 때문이다.
그래서 0부터 시작하는 점수에 (가 등장하면 +1을 )가 등장하면 -1을 하여 0일 될때까지 문자열을 검사하였다.

초기에 주어진 괄호는 이미 균형잡힌 문자열이므로 문자열의 일부가 균형이 잡혀있다면 그 나머지도 균형이 잡히게 된다.

두번째로 올바른 괄호 문자열의 파악은 )가 (보다 선행되는지를 판별하였다.
어떤 괄호 문자열이 균형잡힌 문자열인데, )의 개수가 (보다 많아지는 시점이 존재한다면 올바른 문자열이 아니게 된다.
따라서 균형잡힌 괄호 문자열을 판별하면서 점수가 음수가 되는 시점이 존재하는지를 판별하여 올바른 괄호 문자열을 확인하였다.

마지막으로 괄호의 방향을 뒤집는 방법이 남았다.
기본적으로 문자열에서 치환은 replace함수를 사용하게 된다.
그런데 이 문제에서는 (와 )를 서로 바꿔줘야 하기 때문에 이미 바뀐 괄호를 다시 바꿔주게 되어 한 방향의 괄호만 나타나게 된다.
따라서 한쪽을 임시의 다른 문자열로 치환한 후 반대쪽을 바꿔주고 임시로 치환된 문자열을 바꿔주면 해결이 된다.

## 다른 사람 풀이
그나마 길이가 짧은 풀이.
다른 풀이들을 보면 여러개의 함수를 선언하고 길고 복잡하지만, 이 풀이는 매우 간결하다.
```
def solution(p):
    if p=='': return p
    r=True; c=0
    for i in range(len(p)):
        if p[i]=='(': c-=1
        else: c+=1
        if c>0: r=False
        if c==0:
            if r:
                return p[:i+1]+solution(p[i+1:])
            else:
                return '('+solution(p[i+1:])+')'+''.join(list(map(lambda x:'(' if x==')' else ')',p[1:i]) ))

```
