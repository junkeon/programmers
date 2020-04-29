## 082. 뉴스 클러스터링

## 풀이

모든 글자를 소문자로 바꾼 후 각각의 문자열을 두글자씩 끊는다. 두글자씩 끊어진 것들 중 중복된 것을 제거하고, 끊어진 두글자들의 교집합과 합집합을 구해 자카드 유사도를 계산한다.

## 생각

자카드 유사도를 계산하기 전에 문제 조건에 맞추어 모두 소문자로 변환해주어야 한다.

그런 후에는 유사도 계산을 위해 두글자씩 끊어준다. 이때 하나라도 알파벳이 아닌 문자를 포함하면 제외해주어야 한다.

그리고 다중집합에서의 교집합과 합집합의 수를 세어주어야 하는데, 이를 위해 각각 문자열에서 중복 제거되어 끊어진 두글자들의 교집합과 합집합을 구한다.

그리고 다중집합에서의 교집합은 두 문자열에 모두 포함된 두글자 중 두글자로 끊어진 문자열에서 더 적게 등장한 빈도의 합을 구하면 되고, 합집합은 더 많이 등장한 빈도의 합을 구하면 된다.

## 다른 사람 풀이
나의 풀이에 큰 영향을 준 풀이.
전체적으로 같은 흐름이나, 이 풀이에서 정규표현식을 사용하지 않는 방법으로 구현함
```
import re
import math

def solution(str1, str2):
    str1 = [str1[i:i+2].lower() for i in range(0, len(str1)-1) if not re.findall('[^a-zA-Z]+', str1[i:i+2])]
    str2 = [str2[i:i+2].lower() for i in range(0, len(str2)-1) if not re.findall('[^a-zA-Z]+', str2[i:i+2])]

    gyo = set(str1) & set(str2)
    hap = set(str1) | set(str2)

    if len(hap) == 0 :
        return 65536

    gyo_sum = sum([min(str1.count(gg), str2.count(gg)) for gg in gyo])
    hap_sum = sum([max(str1.count(hh), str2.count(hh)) for hh in hap])

    return math.floor((gyo_sum/hap_sum)*65536)
```
