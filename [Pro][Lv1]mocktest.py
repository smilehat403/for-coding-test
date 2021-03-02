def solution(answers):
    answer = []
    score1 = 0  # 1 2 3 4 5
    score2 = 0  # 2 1 2 3 2 4 2 5
    score3 = 0  # 3 3 1 1 2 2 4 4 5 5 
    
    answer1 = [1,2,3,4,5]; len1 = len(answer1)
    answer2 = [2,1,2,3,2,4,2,5]; len2 = len(answer2)
    answer3 = [3,3,1,1,2,2,4,4,5,5]; len3 = len(answer3)
    
    for i in range(len(answers)):
        if answer1[i%len1] == answers[i]:
            score1 += 1
        if answer2[i%len2] == answers[i]:
            score2 += 1
        if answer3[i%len3] == answers[i]:
            score3 += 1
    
    scores = [score1,score2,score3]
    
    for person, score in enumerate(scores):
        if score == max(scores):
            answer.append(person+1)
    
    
    return answer # 가장 많은 문제를 맞힌 사람, 여럿일 경우 오름차순 정렬