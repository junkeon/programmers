## 049. 문자열 압축

## 풀이

가능한 모든 압축할 수 있는 표현식을 구해서 비교하여 가장 적은 문자열의 수를 리턴한다.

## 생각

압축할 수 있는 문자열의 수를 모두 고려하여 비교하면 되는 문제였다.

처음에는 다른 방법이 있는지 생각해보았으나, 주어진 문자열의 길이가 그리 많지 않았고, 최대로 가능한 것은 문자열의 길이의 절반까지이므로 모든 경우를 비교하는 것이 가능했다.

파이썬의 slicing을 이용하여 주어진 문자열을 쪼개고, 연속된 수를 세어 문자열에 이어 붙여 압축을 진행하였다.

여기서 주의할 점은 개수가 1인 상황은 숫자를 포함하지 않는다는 것이었다.

## 다른 사람 풀이
내 풀이는 for문 안에 slicing으로 풀었지만, 이 풀이는 처음부터 slicing한 리스트를 이용하여 풀었다.
```
def compress(text, tok_len):
    words = [text[i:i+tok_len] for i in range(0, len(text), tok_len)]
    res = []
    cur_word = words[0]
    cur_cnt = 1
    for a, b in zip(words, words[1:] + ['']):
        if a == b:
            cur_cnt += 1
        else:
            res.append([cur_word, cur_cnt])
            cur_word = b
            cur_cnt = 1
    return sum(len(word) + (len(str(cnt)) if cnt > 1 else 0) for word, cnt in res)

def solution(text):
    return min(compress(text, tok_len) for tok_len in list(range(1, int(len(text)/2) + 1)) + [len(text)])
```
