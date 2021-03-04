def solution(bridge_length, weight, truck_weights):
    # 경과시간:int, 다리를 지난 트럭:list, 건너는 트럭:list 대기 트럭:truck_weights
    truck_weights.reverse()  # pop(0)하면 시간 많이 걸려서 뒤집어주기 -> pop()하면 됨
    time = 0
    fin_truck = [];
    ing_truck = []

    tot_truck = len(truck_weights)

    # time ++
    # sum(ing트럭)+(대기 트럭[-1])이 weight보다 작은가? -> 크면 continue
    # 작으면 ing트럭.append(대기트럭.pop())
    # ing 트럭은 언제빠지는가? -> dist = [0][0][0][0][0][0] 배열 설정하고 들어올때마다 차근차근 준다.
    # truck_num = 0하고 들어올때마다 +1
    # 메모리 낭비지만 아이디어가 안떠오름. dict도 메모리는 비슷하게 쓸듯. check = 0 으로 시작해서 
    # dist[check] == 다리길이인지 확인하고 맞으면 fin_트럭.append(ing_truck.pop(0))하고 check+1
    # 언제까지? 다리를 지난 트럭의 갯수가 처음 대기 트럭 수랑 같을 때까지
    dist = [0] * tot_truck
    tag = 0;
    check = 0
    while len(fin_truck) != tot_truck:
        time += 1
        if truck_weights:     # 산으로 가기 시작.... index처리를 못해서... 어쩔 수 없이 넣음.. 점점 복잡해짐
            if sum(ing_truck) + truck_weights[-1] > weight:
                for i in range(check, tag):
                    dist[i] += 1  # 거리를 모두 증가
                if dist[check] == bridge_length:  # check은 언제나 가장 앞에 있는 트럭을 가리킴
                    fin_truck.append(ing_truck.pop(0))  # 가장 앞에 있는 트럭을 fin_truck에 넣어줌
                    check += 1
                continue
        if truck_weights:   # 산으로 가기 시작~
            ing_truck.append(truck_weights.pop())
            tag += 1  # 다리위로 트럭이 들어옴
        for i in range(check, tag):
            dist[i] += 1  # 거리를 모두 증가

        if dist[check] == bridge_length:  # check은 언제나 가장 앞에 있는 트럭을 가리킴
            fin_truck.append(ing_truck.pop(0))  # 가장 앞에 있는 트럭을 fin_truck에 넣어줌
            check += 1
    time += 1   # 내 코드상 마지막에 time+1을 안하고 나와버림
    return time

# print(solution(2,10,[7,4,5,6]))