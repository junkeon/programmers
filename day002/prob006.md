## 006. 2016년

## 풀이

datetime 모듈을 이용하여 요일을 구한다.

## 생각

datetime 모듈을 이용하는 것에 마음이 걸렸지만, 개발자는 바퀴를 새로 만들지 않기 때문에 넘어가기로 한다.

## 다른 사람 풀이

사실 다음의 코드를 의도한 것 같다.

```
def getDayName(a,b):
    months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = ['FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU']
    return days[(sum(months[:a-1])+b-1)%7]
```

그리고...

엄... 엄청나!

```
def bb(b):
    return  b % 7
def solution(a, b):
    if a == 1:
        if bb(b) == 3:
            answer = "SUN"
        elif bb(b) == 4:
            answer = "MON"
        elif bb(b) == 5:
            answer = "TUE"
        elif bb(b) == 6:
            answer = "WED"
        elif bb(b) == 0:
            answer = "THU"
        elif bb(b) == 1:
            answer = "FRI"
        elif bb(b) == 2:
            answer = "SAT"
    if a == 2:
        if bb(b) == 0:
            answer = "SUN"
        elif bb(b) == 1:
            answer = "MON"
        elif bb(b) == 2:
            answer = "TUE"
        elif bb(b) == 3:
            answer = "WED"
        elif bb(b) == 4:
            answer = "THU"
        elif bb(b) == 5:
            answer = "FRI"
        elif bb(b) == 6:
            answer = "SAT"
    if a == 3:
        if bb(b) == 6:
            answer = "SUN"
        elif bb(b) == 0:
            answer = "MON"
        elif bb(b) == 1:
            answer = "TUE"
        elif bb(b) == 2:
            answer = "WED"
        elif bb(b) == 3:
            answer = "THU"
        elif bb(b) == 4:
            answer = "FRI"
        elif bb(b) == 5:
            answer = "SAT"
    if a == 4:
        if bb(b) == 3:
            answer = "SUN"
        elif bb(b) == 4:
            answer = "MON"
        elif bb(b) == 5:
            answer = "TUE"
        elif bb(b) == 6:
            answer = "WED"
        elif bb(b) == 0:
            answer = "THU"
        elif bb(b) == 1:
            answer = "FRI"
        elif bb(b) == 2:
            answer = "SAT"
    if a == 5:
        if bb(b) == 1:
            answer = "SUN"
        elif bb(b) == 2:
            answer = "MON"
        elif bb(b) == 3:
            answer = "TUE"
        elif bb(b) == 4:
            answer = "WED"
        elif bb(b) == 5:
            answer = "THU"
        elif bb(b) == 6:
            answer = "FRI"
        elif bb(b) == 0:
            answer = "SAT"
    if a == 6:
        if bb(b) == 5:
            answer = "SUN"
        elif bb(b) == 6:
            answer = "MON"
        elif bb(b) == 0:
            answer = "TUE"
        elif bb(b) == 1:
            answer = "WED"
        elif bb(b) == 2:
            answer = "THU"
        elif bb(b) == 3:
            answer = "FRI"
        elif bb(b) == 4:
            answer = "SAT"
    if a == 7:
        if bb(b) == 3:
            answer = "SUN"
        elif bb(b) == 4:
            answer = "MON"
        elif bb(b) == 5:
            answer = "TUE"
        elif bb(b) == 6:
            answer = "WED"
        elif bb(b) == 0:
            answer = "THU"
        elif bb(b) == 1:
            answer = "FRI"
        elif bb(b) == 2:
            answer = "SAT"
    if a == 8:
        if bb(b) == 0:
            answer = "SUN"
        elif bb(b) == 1:
            answer = "MON"
        elif bb(b) == 2:
            answer = "TUE"
        elif bb(b) == 3:
            answer = "WED"
        elif bb(b) == 4:
            answer = "THU"
        elif bb(b) == 5:
            answer = "FRI"
        elif bb(b) == 6:
            answer = "SAT"
    if a == 9:
        if bb(b) == 4:
            answer = "SUN"
        elif bb(b) == 5:
            answer = "MON"
        elif bb(b) == 6:
            answer = "TUE"
        elif bb(b) == 0:
            answer = "WED"
        elif bb(b) == 1:
            answer = "THU"
        elif bb(b) == 2:
            answer = "FRI"
        elif bb(b) == 3:
            answer = "SAT"
    if a == 10:
        if bb(b) == 2:
            answer = "SUN"
        elif bb(b) == 3:
            answer = "MON"
        elif bb(b) == 4:
            answer = "TUE"
        elif bb(b) == 5:
            answer = "WED"
        elif bb(b) == 6:
            answer = "THU"
        elif bb(b) == 0:
            answer = "FRI"
        elif bb(b) == 1:
            answer = "SAT"
    if a == 11:
        if bb(b) == 6:
            answer = "SUN"
        elif bb(b) == 0:
            answer = "MON"
        elif bb(b) == 1:
            answer = "TUE"
        elif bb(b) == 2:
            answer = "WED"
        elif bb(b) == 3:
            answer = "THU"
        elif bb(b) == 4:
            answer = "FRI"
        elif bb(b) == 5:
            answer = "SAT"
    if a == 12:
        if bb(b) == 4:
            answer = "SUN"
        elif bb(b) == 5:
            answer = "MON"
        elif bb(b) == 6:
            answer = "TUE"
        elif bb(b) == 0:
            answer = "WED"
        elif bb(b) == 1:
            answer = "THU"
        elif bb(b) == 2:
            answer = "FRI"
        elif bb(b) == 3:
            answer = "SAT"
    return answer
```
