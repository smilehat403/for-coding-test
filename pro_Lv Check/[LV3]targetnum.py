def solution(begin, target, words):
    global answer
    answer = 9876
    if target not in words:
        return 0
    
    def check_diff(s1:str,s2:str):
        length = len(s1)
        cnt = 0
        for i in range(length):
            if s1[i] != s2[i]:
                cnt += 1
        if cnt == 1:
            return True
        return False
    
    visited=[0]*len(words)
    
    def dfs(start:str,idx):
        global answer
        if start == target:
            answer = min(answer,idx)
        
        for i in range(len(words)):
            if check_diff(words[i], start) and (visited[i] == 0):
                visited[i] = 1
                dfs(words[i],idx+1)
                visited[i] = 0
    
    dfs(begin,0)
    
    return answer