# 초 단위로 기록된 주식가격
def solution(prices):
    # 가격이 떨어지지 않은 기간
    answer = []
    length = len(prices)
    for idx in range(length):
        cnt = -1
        for jdx in range(idx,length):
            if prices[idx] <= prices[jdx]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer