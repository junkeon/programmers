import datetime

def solution(a, b):
    days = ['MON','TUE','WED','THU','FRI','SAT', 'SUN']
    d = datetime.datetime(2016, a, b)
    
    answer = days[d.weekday()]
    return answer