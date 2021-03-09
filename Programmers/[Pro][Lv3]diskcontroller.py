import heapq

def solution(jobs):
    jlen = len(jobs)
    # jobs에서 뺀다음 que에 실행시간을 기준으로 최소힙
    time, something_start, que = 0,-1,[]
    # 완료한 프로세스
    exit = 0
    answer = 0
    while exit <jlen:
        for rq_rt in jobs:
            # r = requset, rt = runtime
            # 컴퓨터는 한번에 한가지 일만 가능 -> something_start < 실행입력시간
            # 현재 시간보다는 전에 입력돼야함 -> 실행입력시간 <= 현재시간(time)
            if something_start < rq_rt[0] <= time:  
                # 현재 시간 기준, 프로세스가 que에 들어가서 얼마나 기다렸는가
                answer += time - rq_rt[0]
                # runtime 최소힙으로 que에 넣는다
                heapq.heappush(que,rq_rt[1])
        if que:
            # sj이 끝날 때까지 que에 있는 프로세스는 전부 대기중
            answer += len(que)*que[0]
            # process 완료 -> endpoint를 현시간으로 지정
            something_start = time
            # sj를 더해준다
            time += heapq.heappop(que)
            # 완료 상태 +1
            exit += 1
        else : # que가 비어있을때
            time += 1
    return answer//jlen

# jobs = [[0,3],[1,9],[2,6]]
# solution(jobs)