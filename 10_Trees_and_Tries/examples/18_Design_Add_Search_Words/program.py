"""LC 211 - Design Add and Search Words"""
class TrieNode:
    def __init__(self): self.ch={}; self.end=False
class WordDictionary:
    def __init__(self): self.root=TrieNode()
    def addWord(self,word):
        node=self.root
        for c in word: node=node.ch.setdefault(c,TrieNode())
        node.end=True
    def search(self,word):
        def dfs(idx,node):
            if idx==len(word): return node.end
            c=word[idx]
            if c=='.':
                return any(dfs(idx+1,child) for child in node.ch.values())
            if c not in node.ch: return False
            return dfs(idx+1,node.ch[c])
        return dfs(0,self.root)
if __name__=="__main__":
    wd=WordDictionary()
    for w in ["bad","dad","mad"]: wd.addWord(w)
    tests=[("pad",False),("bad",True),(".ad",True),("b..",True),("...",True),("ba",False)]
    for word,expected in tests:
        result=wd.search(word)
        print(f"search('{word}') = {result} {'✓' if result==expected else '✗'}")
