# Example 14: Word Ladder (LC 127)
## Problem
Transform beginWord to endWord by changing one letter at a time (each intermediate must be in wordList). Return number of steps.
## Input
beginWord="hit", endWord="cog", wordList=["hot","dot","dog","lot","log","cog"]
## Output
5
## Approach
BFS: each state = current word. Neighbors = all 1-letter variants in wordList.
**Time: O(M²×N)  Space: O(M²×N)**