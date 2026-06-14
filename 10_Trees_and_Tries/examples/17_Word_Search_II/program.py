"""LC 212 - Word Search II"""
class TrieNode:
    def __init__(self): self.ch={}; self.word=None

def find_words(board, words):
    root=TrieNode()
    for w in words:
        node=root
        for c in w: node=node.ch.setdefault(c,TrieNode())
        node.word=w
    rows,cols=len(board),len(board[0])
    result=[]
    def dfs(r,c,node):
        char=board[r][c]
        if char not in node.ch: return
        nxt=node.ch[char]
        if nxt.word: result.append(nxt.word);nxt.word=None
        board[r][c]='#'
        for dr,dc in [(0,1),(0,-1),(1,0),(-1,0)]:
            nr,nc=r+dr,c+dc
            if 0<=nr<rows and 0<=nc<cols and board[nr][nc]!='#':
                dfs(nr,nc,nxt)
        board[r][c]=char
    for r in range(rows):
        for c in range(cols): dfs(r,c,root)
    return result

if __name__=="__main__":
    board=[["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]]
    words=["oath","pea","eat","rain"]
    print(find_words(board,words))
