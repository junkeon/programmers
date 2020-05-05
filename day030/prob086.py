def convert_notes(notes):
    notes = notes.replace('C#', 'c')
    notes = notes.replace('D#', 'd')
    notes = notes.replace('F#', 'f')
    notes = notes.replace('G#', 'g')
    notes = notes.replace('A#', 'a')
    return notes

def convert_time(tic):
    h, m = tic.split(':')
    return int(h)*60 + int(m)

def solution(m, musicinfos):
    candi = []
    m = convert_notes(m)

    for music in musicinfos:
        start, end, title, notes = music.split(',')
        notes = convert_notes(notes)
        
        duration = convert_time(end) - convert_time(start)
        notes = notes * (duration // len(notes)) + notes[:duration%len(notes)]

        if m in notes:
            candi.append((len(notes), title))
            
    if not candi:
        return '(None)'
    
    *_, answer = max(candi, key = lambda x:x[0])
    return answer
