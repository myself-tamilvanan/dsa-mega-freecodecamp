"""LC 547 - Number of Provinces"""
def find_circle_num(isConnected):
    n=len(isConnected)
    visited=set()
    def dfs(i):
        for j in range(n):
            if isConnected[i][j]==1 and j not in visited:
                visited.add(j); dfs(j)
    count=0
    for i in range(n):
        if i not in visited:
            visited.add(i); dfs(i); count+=1
    return count
if __name__=="__main__":
    cases=[([[1,1,0],[1,1,0],[0,0,1]],2),([[1,0,0],[0,1,0],[0,0,1]],3),([[1,1,0],[1,1,1],[0,1,1]],1)]
    for matrix,expected in cases:
        result=find_circle_num(matrix)
        print(f"Provinces={result} {'✓' if result==expected else '✗'}")
