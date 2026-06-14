"""LC 787 - Cheapest Flights Within K Stops"""
def find_cheapest_price(n, flights, src, dst, k):
    # Bellman-Ford: relax edges k+1 times
    prices=[float('inf')]*n
    prices[src]=0
    for _ in range(k+1):
        temp=prices[:]
        for u,v,w in flights:
            if prices[u]!=float('inf') and prices[u]+w<temp[v]:
                temp[v]=prices[u]+w
        prices=temp
    return prices[dst] if prices[dst]!=float('inf') else -1
if __name__=="__main__":
    cases=[(4,[[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]],0,3,1,700),(3,[[0,1,100],[1,2,100],[0,2,500]],0,2,0,500)]
    for n,f,src,dst,k,expected in cases:
        result=find_cheapest_price(n,f,src,dst,k)
        print(f"src={src},dst={dst},k={k} -> {result} {'✓' if result==expected else '✗'}")
