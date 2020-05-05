## 086. 방금그곡

## 풀이

샵을 가진 음표를 치환한 후 곡 정보들과 비교하여 재생된 음표들과 멜로디를 비교하여 매칭 여부를 판단하고, 가장 재생 시간이 긴 곡의 제목을 리턴한다.

## 생각

멜로디에서는 샵이 포함된 문자열을 다루다보니 매칭여부와 길이 계산에 어려움이 있었다. 따라서 이런 점을 개선하고자 X#의 문자열을 x로 치환하여 하나의 문자열로 만들었다.

그 다음에는 곡정보에서 시작 시간, 끝시간, 제목, 음표들을 분리하고 마찬가지로 음표들에서 #을 제거하였다. 그런 후에는 시간 정보를 토대로 재생 시간을 계산하고 문제 조건에 맞춰 음악 길이에 따른 음표들을 재정렬하였다.

그런 후에 기억하는 멜로디와의 매칭 여부를 판단하여 후보군에 저장한 후, 길이를 비교하여 가장 긴 음악의 제목을 리턴하였다.

## 다른 사람 풀이
출처 : https://m.blog.naver.com/jaeyoon_95/221758073646
문제를 풀면서 해멜때 도움을 받은 코드이다.
특히 # 문자열과 재생시간에 대한 음표들을 계산하는데 도움을 받았다.
```
def solution(m, musicinfos):
    m = m.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
    music_dic = dict()
    answer = ["",""]
    for information in musicinfos:
        start, end, name, music = information.split(',')
        music = music.replace('C#','c').replace('D#','d').replace('E#','e').replace('F#','f').replace('G#','g').replace('A#','a')
        start =[int(time) for time in start.split(':')]
        end = [int(time) for time in end.split(':')]
        all_time = (end[0]-start[0])*60 + (end[1]-start[1])
        music = music*(all_time//len(music)) + music[0:all_time%len(music)]
        music_dic[name] = music
    for key,value in music_dic.items():
        if m in value:
            if len(answer[1]) < len(value): 
                answer[0] = key
                answer[1] = value
    return "(None)" if len(answer[0]) == 0 else answer[0]
```
