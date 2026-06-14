"""LC 208 - Implement Trie (Design Chapter variant)"""
class TrieNode:
    def __init__(self): self.ch={}; self.end=False
class Trie:
    def __init__(self): self.root=TrieNode()
    def insert(self,word):
        n=self.root
        for c in word: n=n.ch.setdefault(c,TrieNode())
        n.end=True
    def search(self,word):
        n=self.root
        for c in word:
            if c not in n.ch: return False
            n=n.ch[c]
        return n.end
    def startsWith(self,prefix):
        n=self.root
        for c in prefix:
            if c not in n.ch: return False
            n=n.ch[c]
        return True
if __name__=="__main__":
    t=Trie()
    words=["apple","app","application","ball","bat"]
    for w in words: t.insert(w)
    tests=[("apple",True),("app",True),("ap",False),("b",False),("ba",False),("ball",True)]
    for word,expected in tests:
        result=t.search(word)
        print(f"search('{word}')={result} {'✓' if result==expected else '✗'}")
    prefixes=["ap","app","b","xyz","ba"]
    for p in prefixes:
        print(f"startsWith('{p}')={t.startsWith(p)}")
