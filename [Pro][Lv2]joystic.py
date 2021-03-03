def solution(name):
    answer = 0
    # "ABCDE" -> "01234"
    al_to_num = [min(ord(alpha)-ord('A'),ord('Z')-ord(alpha)+1) for alpha in name]
    i = 0
    
    while True:
        # 알파벳 바꾸기, 0으로 초기화
        answer += al_to_num[i]
        al_to_num[i] = 0
        
        # 싹다 0으로 처리됐으면
        if sum(al_to_num) == 0:
            return answer
        
        lpoint, rpoint = 1,1
        while al_to_num[i-lpoint] == 0:
            lpoint += 1
        while al_to_num[i+rpoint] == 0:
            rpoint += 1
        
        if lpoint<rpoint:
            answer += lpoint
            i -= lpoint
        else:
            answer += rpoint
            i += rpoint