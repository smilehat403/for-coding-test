class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        output = []
        answer = []
        
        def dfs(now,idx):
            if now < 0 :
                return
            if now == 0 :
                output.append(answer[:])
                return
            
            for i in range(idx,len(candidates)):
                answer.append(candidates[i])
                dfs(now-candidates[i],i)
                answer.pop()
                # dfs(now-candidates[i],i,answer+[candidates[i]]) <- append,pop을 안해도됨
        
        dfs(target,0)
        
        return output
        