def solution(brown, yellow):
    answer = []
    total = brown+yellow
    for i in range(3,total//2):
        if (total%i==0) and (yellow%(i-2)==0):
            answer = [i, total/i]
    answer.sort(reverse = True)
    
    return answer   # 가로, 세로 >> 가로 길이 >= 세로 길이