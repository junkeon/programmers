## 064. 가장 큰 정사각형 찾기

## 풀이

DP 기반으로 현재 위치를 꼭지점으로 하는 최대 정사각형의 길이를 저장하는 memoization으로 푼다.

## 생각

DP를 사용해서 푸는 문제이다.

score라는 memoization table을 만들고, 각 점의 값은 현재 위치를 0, 0을 시작으로 하여 우측 하단의 꼭지점으로 하는 최대 정사각형의 길이를 저장하게 한다.

이때 이 값을 저장하기 위한 식은 현재 위치의 board 값이 1인 경우에, 좌측 상단, 좌측, 상측의 score값 중 최소값에서 1을 더한 값이 된다.

이렇게 되면 좌측 상단, 좌측, 상측이 같은 길이의 정사각형의 꼭지점이 될때에 현재 위치가 그보다 1이 늘어난 정사각형의 꼭지점이 되기 때문이다.

이런 식으로 memoization table을 구성한 후 가장 큰 값의 제곱을 하면 최대의 정사각형의 크기가 된다.

## 다른 사람 풀이
아무리 봐도 내 풀이보다 더 간결하거나 나은 풀이가 없는 것 같아 패스
```

```
