# Example 17: Reconstruct Itinerary (LC 332)
## Problem
Given airline tickets [from,to], reconstruct itinerary starting from JFK using all tickets. Lexically smallest.
## Input
tickets=[["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]] → ["JFK","MUC","LHR","SFO","SJC"]
## Approach
Hierholzer's algorithm (Eulerian path) with sorted adjacency list.
**Time: O(E log E)  Space: O(E)**