import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        if scoville[0]>=K:
            return answer
        min1st = heapq.heappop(scoville)
        if not scoville:
            return -1
        min2nd = heapq.heappop(scoville)
        heapq.heappush(scoville, min1st+min2nd*2)
        answer += 1
    return -1