## 081. 예상 대진표

## 풀이

주어진 수들에서 1을 뺀 수들을 이진법으로 나타내었을 때, 가장 앞자리수부터 비교를 하여 다른 자리수를 리턴한다.

## 생각

2의 지수승의 참가자가 경쟁을 하여 토너먼트를 진행하면 각 참가자의 순번을 2진법으로 나타냈을 때 첫번째 라운드에서는 앞의 모든 자리수가 동일하고 마지막만 다른 순번을 가진 참가자들과 붙게 된다.

이후 두번째 라운드에서는 뒤에서 두번째 자리수가 다른 참가자와 붙게 된다.

이를 일반화하여 참가자의 순번(0부터 시작하므로 1을 빼줌)을 2진법으로 나타냈을 때, 앞 자리부터 가장 차이가 나는 자리수만큼의 라운드가 지난 후에 그 참가자와 붙게 된다.

따라서 2진법으로 바꾼후 앞자리수부터 비교하면 된다.

## 다른 사람 풀이
하... 하아...
```
def solution(n,a,b):
    return ((a-1)^(b-1)).bit_length()
```