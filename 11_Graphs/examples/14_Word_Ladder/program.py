"""LC 127 - Word Ladder"""
from collections import deque

def ladder_length(beginWord, endWord, wordList):
    word_set=set(wordList)
    if endWord not in word_set: return 0
    q=deque([(beginWord,1)])
    visited={beginWord}
    while q:
        word,steps=q.popleft()
        for i in range(len(word)):
            for c in 'abcdefghijklmnopqrstuvwxyz':
                new_word=word[:i]+c+word[i+1:]
                if new_word==endWord: return steps+1
                if new_word in word_set and new_word not in visited:
                    visited.add(new_word);q.append((new_word,steps+1))
    return 0
if __name__=="__main__":
    cases=[("hit","cog",["hot","dot","dog","lot","log","cog"],5),("hit","cog",["hot","dot","dog","lot","log"],0)]
    for bw,ew,wl,expected in cases:
        result=ladder_length(bw,ew,wl)
        print(f"'{bw}'->'{ew}': {result} steps {'✓' if result==expected else '✗'}")
