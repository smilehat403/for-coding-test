import collections
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = collections.defaultdict(list)
        for depart, arrival in sorted(tickets,reverse = True):
            graph[depart].append(arrival)
        
        route = []
        
        def dfs(dpt):
            while graph[dpt]:
                dfs(graph[dpt].pop())
            route.append(dpt)
        
        dfs("JFK")
        
        return route[::-1]