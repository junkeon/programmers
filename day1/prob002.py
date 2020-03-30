def solution(answers):
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt = [0, 0, 0]
    for i, ans in enumerate(answers):
        if ans == student_1[i%len(student_1)]:
            cnt[0] += 1
        if ans == student_2[i%len(student_2)]:
            cnt[1] += 1
        if ans == student_3[i%len(student_3)]:
            cnt[2] += 1
            
    answer = []
    for i in range(3):
        if cnt[i] == max(cnt):
            answer.append(i+1)
            
    return answer