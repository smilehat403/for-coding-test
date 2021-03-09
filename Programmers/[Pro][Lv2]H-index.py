def solution(citations):
    answer = 0
    # 3 0 6 1 5 -> 6 5 3 // 1 0
    # len(왼쪽 그룹) >= 왼쪽 그룹의 최소 성분
    # 최댓값을 찾는 거기 때문에 정렬한 다음 0부터 1씩 늘려나가다
    # 조건 만족하면 break
#   ㄹㅇ 멍청.... [9,5,1] 같은 케이스에는 해당 사항이 안됨
#   h_idx = [0][0][0] 배열은 n번째까지 끊을 때 h-index가 몇인지 보여주는 지표
#   h_idx = [1][2][0] 임을 알 수 있음
    paper_num = len(citations)
    h_idx = [0]*paper_num
    citations.sort(reverse = True)
    for i in range(paper_num):
        if  citations[i] >= len(citations[:i+1]):
            h_idx[i] = i+1
    answer = max(h_idx)
    return answer

# citations = [9,5,1]
# print(solution(citations))