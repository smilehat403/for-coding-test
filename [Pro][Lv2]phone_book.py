def solution(phone_book):
    answer = True
    # answer.sort() -> 문자열을 정렬할 경우 앞의 숫자를 비교하면서 정렬
    # sort_ans = sorted(phone_book)로 해야함
    # ["12","123","1235","567","88"] <- 이건 정렬이 된거임
    # ["123","456","789"] 여기서 123(i=1) 다음 숫자(i=2)가 123을 접두어로 가지고 있지 않은데
    # 그 다다음 숫자(i=3)이 123을 접두어로 가질까? ㄴㄴ
    
    sort_ans = sorted(phone_book)
    for i in range(len(sort_ans)-1):
        if sort_ans[i] == sort_ans[i+1][:len(sort_ans[i])]:
            answer = False
            break
    
    return answer


######## 엄청 파이썬스러운 풀이 ##########
def solution(phoneBook):
    phoneBook = sorted(phoneBook)

    for p1, p2 in zip(phoneBook, phoneBook[1:]):
        if p2.startswith(p1):
            return False
    return True