"""LC 208 - Implement Trie"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self): self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
        node.is_end = True

    def search(self, word):
        node = self.root
        for c in word:
            if c not in node.children: return False
            node = node.children[c]
        return node.is_end

    def startsWith(self, prefix):
        node = self.root
        for c in prefix:
            if c not in node.children: return False
            node = node.children[c]
        return True

if __name__ == "__main__":
    trie = Trie()
    words = ["apple", "app", "application", "apply"]
    for w in words: trie.insert(w)
    tests = [("apple",True), ("app",True), ("ap",False), ("application",True), ("appl",False)]
    for word, expected in tests:
        result = trie.search(word)
        print(f"search('{word}') = {result} {'✓' if result==expected else '✗'}")
    print(f"startsWith('app') = {trie.startsWith('app')}")
    print(f"startsWith('xyz') = {trie.startsWith('xyz')}")
