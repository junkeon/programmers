## 011. 문자열 내 마음대로 정렬하기

## 풀이

주어진 리스트를 우선 사전식으로 정렬한 후 n번째 char을 기준으로 다시 정렬해준다.

## 생각

최근에 들어서야 lambda에 익숙해졌다.
물론 익숙해져서 아주 간단한 것에만 사용할 수 있다는 것이지, 복잡한 것에 응용은 어렵다.
이 lambda를 이용한 정렬은 딕셔너리 정렬에서 필요해서 배우게 되었다.
그리고 최근에서야 다른 자료형에 응용할 수 있었다.

이 lambda는 map과 같은 함수를 이용할  때 더 빛을 발하는 거 같은데, 난 아직 sort에 밖에 사용하지 못한다.
좀더 잘 사용하여 멋진 코드를 짤 수 있기를 바란다.

그리고 다른 사람 풀이를 보면서 이런 생각을 하게 되었다.
'만약 sort를 두 번 쓰지 않고 모든 걸 내가 짜야 한다면 어떻게 짤 수 있을까?'
많은 사람들이 현재 내 코드와 같이 sort를 두 번 이용한 간단한 풀이를 냈기에, 나라면 어떻게 했을까를 고민해보았다.

## 다른 사람 풀이

풀다 보니까 어째든 두 번의 sort를 쓰게 됩니다.
이건 sort를 안 쓴 풀이가 아닌 comprehension을 안 쓴 풀이라고 합시다.

```
def solution(strings, n):    
    key_dict = dict()
    for word in strings:
        key = word[n]
        if key not in key_dict:
            key_dict[key] = [word]
        else:
            key_dict[key].append(word)
			
    answer = []
    for key in sorted(key_dict.keys()):
        answer.extend(sorted(key_dict[key]))
		
    return answer
```