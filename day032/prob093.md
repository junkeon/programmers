## 093. 섬 연결하기

## 풀이

Prim algorithm을 이용하여 MST로 최소 비용을 구한다.

## 생각

MST는 Minimum Spanning Tree로 가중치 그래프에서 모든 노트를 포함한 연결된 부분 그래프를 찾아내는 문제이다.

그 중에서 Prim 알고리즘은 MST를 푸는 가장 대표적인 알고리즘이다.

Prim 알고리즘은 다음의 과정을 거친다.

0. 시작 노드를 선택한다. (임의의 노드 선택 가능)

1. 현재 이어진 부분 그래프에서 가능한 모든 연결을 탐색한다.

2. 가능한 모든 연결 중에서 가장 적은 가중치(비용)을 갖는 노드를 선택한다.

3. 2에서 선택한 노드와 이어준다.

4. 모든 노드가 이어질 때까지 1번으로 돌아가 과정을 반복한다.

이 Prim 알고리즘을 구현하면서 2번 과정에서 어떤 알고리즘으로 가장 적은 가중치를 찾는지에 따라 성능이 달라진다.

가장 간단하면서도 효율적인 방법은 heap queue를 이용하는 것이다.

따라서 1번에서 가능한 연결을 heap push로 넣고 2번에서 heap pop으로 가능한 연결을 탐색한다.


## 다른 사람 풀이
다른 사람들도 prim 알고리즘을 풀었다.

하지만 구현하는 과정에서 나의 풀이가 가장 깔끔하다고 생각한다.

고로 pass
```

```
