"""LC 332 - Reconstruct Itinerary"""
from collections import defaultdict
import heapq

def find_itinerary(tickets):
    graph=defaultdict(list)
    for src,dst in sorted(tickets,reverse=True):
        graph[src].append(dst)
    for k in graph: graph[k].sort(reverse=True)  # sorted for lexical order
    result=[]
    def dfs(airport):
        while graph[airport]:
            dfs(graph[airport].pop())
        result.append(airport)
    dfs("JFK")
    return result[::-1]
if __name__=="__main__":
    cases=[
        ([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]],["JFK","MUC","LHR","SFO","SJC"]),
        ([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]],["JFK","ATL","JFK","SFO","ATL","SFO"]),
    ]
    for tickets,expected in cases:
        result=find_itinerary(tickets)
        print(f"Result: {result} {'✓' if result==expected else '✗'}")
