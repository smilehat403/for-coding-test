import collections
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = collections.defaultdict(list)
        for start,dest,cost in flights:
            graph[start].append((dest, cost))
            
        k = 0
        que = [(0,src,k)]
        
        while que:
            price, node, k = heapq.heappop(que)
            if node == dst:
                return price
            if k <= K :
                k += 1
                for next_node, cost in graph[node]:
                    alt = price + cost
                    heapq.heappush(que,(alt,next_node,k))
        return -1
         
        
        