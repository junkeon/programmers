## 057. H-Index

## 풀이

citations을 역정렬한 후 현재 인용수와 순번을 비교하여 순번이 높으면 그 이전 순번을 리턴하고, 끝까지 인용수가 높으면 전체 인용된 논문을 리턴한다.

## 생각

생각보다 간단한 문제였고, 간단하게 풀었다 (심지어 핸폰으로 문제 풀음... ㅎ)

우선 인용된 논문 편수랑 인용횟수랑 비교하여 최댓값을 찾아내야 하므로 논문 인용횟수를 역정렬하였고, 논문 편수랑 인용횟수랑 비교하기 위해 for문을 돌려 비교하였다.

여기서 문제는 비교는 하되 h번 이상 인용된 논문이 h 편 이상이고 나머지 논문이 h번 이하로 인용된 h를 찾기 위해 사실상 그 다음 논문의 인용횟수를 알아야 했다.
그래서 for문의 한 스텝 더 돌아서 비교를 하고 만약 현재 인용 횟수랑 인용 편수를 비교하여 인용 편수가 더 크다면 그 이전의 값이 h가 되어야 했다.

그리고 만약에 모든 인용수를 비교했을때 각각의 인용편수보다 크면 전체 인용수가 리턴되어야 했다.

## 다른 사람 풀이
헐...

```
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
```
