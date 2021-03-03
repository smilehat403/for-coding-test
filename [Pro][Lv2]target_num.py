def dfs(result,numbers,target,index):
    global answer   # 여기에도 꼭! global answer 써줘야함
    if index == len(numbers):
        if result == target:
            answer += 1
    else:   # else없이 하면 indx가 초과됨
        dfs(result - numbers[index],numbers,target,index+1)
        dfs(result + numbers[index],numbers,target,index+1)
    
    
def solution(numbers, target):
    global answer
    result, answer = 0, 0
    # 굳이 result 할당 안하고 0, numbers, target, 0만 해도됨
    dfs(result,numbers,target,0)  
    
    return answer