def solution(triangle):
    answer = 0
    # 7
    # 3 8
    # 8 1 0
    # 2 7 4 4
    # 4 5 2 6 5     -> 아래랑 오른쪽으로만 갈 수 있다 라고 생각
    dp = triangle[:]    # 전체 복사
    for row in range(1,len(triangle)):
        for col in range(len(triangle[row])):
            if col == 0:
                tmp = triangle[row-1][col]
            elif col == len(triangle[row])-1:
                tmp = triangle[row-1][col-1]
            else:
                tmp = max(triangle[row-1][col-1],triangle[row-1][col])
            triangle[row][col] += tmp
    answer = max(triangle[len(triangle)-1])
    
    return answer