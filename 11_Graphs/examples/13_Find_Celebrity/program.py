"""LC 277 - Find the Celebrity"""
def find_celebrity(n, knows_matrix):
    def knows(a,b): return knows_matrix[a][b]
    candidate=0
    for i in range(1,n):
        if knows(candidate,i): candidate=i
    for i in range(n):
        if i==candidate: continue
        if knows(candidate,i) or not knows(i,candidate): return -1
    return candidate
if __name__=="__main__":
    matrix1=[[False,True,True],[False,False,True],[False,False,False]]
    print("Celebrity:", find_celebrity(3,matrix1))  # 2
    matrix2=[[False,True],[True,False]]
    print("Celebrity:", find_celebrity(2,matrix2))  # -1
