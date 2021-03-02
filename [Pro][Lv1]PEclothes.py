def solution(n, lost, reserve): # 전체 학생의 수, 도난당한 학생들의 번호, 여벌의 체육복이 있는 학생들
    answer = 0
    # 여벌옷을 가져온 학생이 도난당한 경우 전처리
    set_lost = set(lost)-set(reserve)
    set_reserve = set(reserve)-set(lost)
    
    for stu_index in set_reserve:
        if stu_index-1 in set_lost:
            set_lost.remove(stu_index-1)
        elif stu_index+1 in set_lost:
            set_lost.remove(stu_index+1)
    
    answer = n-len(set_lost)
    
    return answer