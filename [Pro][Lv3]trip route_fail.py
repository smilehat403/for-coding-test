def dfs(now, answer, tickets, visited):
    answer.append(now)
    stacks = []
    stacks.append(now)

    while True:
        depart = stacks.pop()
        if sum(visited) == len(tickets):
            break
        tmp = []
        for idx, ticket in enumerate(tickets):
            if not visited[idx] and ticket[0] == depart:
                tmp.append([idx,ticket[1]])
        tmp.sort(key=lambda x:x[1])
        visited[tmp[0][0]] = 1
        answer.append(tmp[0][1])
        stacks.append(tmp[0][1])

def solution(tickets):
    answer = []
    visited = [0] * len(tickets)
    # 왠지는 모르겠지만 알파벳 순이라길래 도착지를 중심으로 sort함
    # tickets = sorted(tickets, key=lambda x: x[1])
    dfs("ICN", answer, tickets, visited)

    return answer

tickets = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
solution(tickets)