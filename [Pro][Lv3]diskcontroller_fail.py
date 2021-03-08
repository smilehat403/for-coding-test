def solution(jobs):
    answer = 0
    # 멀리 보지말고 항상 요청부터 종료까지 제일 빠른걸 고른다.
    # 1번 경우 : endpoint 3, 12, 18
    # 2번 경우 : endpoint 3, 9, 18
    # jobs에서 endpoint가 가장 짧은 녀석을 고른다.
    # abs(endpoint-rn) + tn이 짧은 녀석을 고른다
    # -> 일반화 endpoint = 0 에서 시작 -> 매번 가장 작은 abs(endpoint-rn)+tn을 구한다
    # sum = 0 -> sum += endpoint - rn
    endpoint = 0;
    total = 0
    length = len(jobs)
    for _ in range(length):
        tmp_ep = 999999
        tmp_rn = []
        for rn_tn in jobs:
            tmptmp_ep = tmp_ep
            if rn_tn[0] <= endpoint:
                tmp_ep = min(tmp_ep, endpoint+ rn_tn[1])
            else:
                tmp_ep = min(tmp_ep, rn_tn[0]+rn_tn[1])

            if tmptmp_ep != tmp_ep:
                tmp_rn = rn_tn
        endpoint = tmp_ep
        total += endpoint - tmp_rn[0]
        jobs.remove(tmp_rn)
    answer = total // length

    return answer

# jobs = [[0, 3], [1, 9], [2, 6]]
# solution(jobs)


