import collections
import heapq 
from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = collections.defaultdict(list)
        for u,v,w in times:
            graph[u].append((v,w))
            
        minheap = [(0, k)]   # k부터 거리, node
        distance = collections.defaultdict(int)
        
        
        while minheap:
            cost, node = heapq.heappop(minheap)
            if node not in distance:
                distance[node] = cost
                for next_node,dist in graph[node]:
                    dist_from_k = cost + dist
                    heapq.heappush(minheap,(dist_from_k,next_node))
        
        if len(distance)  == n:
            return max(distance.values())
        return -1
            