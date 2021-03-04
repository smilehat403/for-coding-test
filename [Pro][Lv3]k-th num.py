def solution(array, commands):
    answer = []
    # temp = array[i-1:j] <- slicing
    # temp.sort() <- sort
    # temp[k-1]
    # 위 방식 반복 -> for command in commands:
    # i,j,k = command <- 이거 맞나?
    # ...
    # answer.append(temp[k-1])
    
    for command in commands:
        i,j,k = command
        temp = array[i-1:j]
        temp.sort()
        answer.append(temp[k-1])
        
    return answer