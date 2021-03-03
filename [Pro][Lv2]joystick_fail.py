# testcase5 실패
def solution(name):
    answer = 0
    # A B C D E F G H I J K  L  M  N  O  P  Q  R S T U V W X Y Z
    # 0 1 2 3 4 5 6 7 8 9 10 11 12 13 12 11 10 9 8 7 6 5 4 3 2 1
    # Dic으로 푸는게 계산시간을 줄일 수 있다고 생각
    from_a = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10,
              'L': 11, 'M': 12, 'N': 13, 'O': 12, 'P': 11, 'Q': 10, 'R': 9, 'S': 8, 'T': 7, 'U': 6, 'V': 5,
              'W': 4, 'X': 3, 'Y': 2, 'Z': 1}
    for alpha in name:
        answer += from_a[alpha]

    # ABAAJ처럼 ->갔다가 <-로 돌아가는 경우 시작하는 A만큼 move_cnt에서 더해줘야함
    first_a = 0
    for alp in name:
        if alp == 'A':
            first_a += 1
        else:
            break
    # BBAAAAAAAABA 인 경우도 신경써줘야함
    # rname = name[::-1]
    # for alp in rname:
    #     if alp == 'A':
    #         first_a += 1
    #     else:
    #         break
            
    move_cnt = 654321   # 최솟값을 구할 때는 항상 초깃값을 크게
    for j in range(len(name)):  # len(name) len! 신경쓸것
        tmp_cnt = 0
        for i in range(len(name)):
            if name[i] != 'A':
                tmp_cnt = i
        move_cnt = min(move_cnt, tmp_cnt)
        # 순환하기 때문에 ABC -> BCA해도 상관없음, 앞에 A있는건 예외처리함
        name = name[1:] + name[0]
    answer += move_cnt + first_a
    return answer

# name = "AABAAAAAAABBB"
# print(solution(name))