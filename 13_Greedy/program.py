"""Chapter 13: Greedy"""

def can_jump(nums):
    reach=0
    for i,n in enumerate(nums):
        if i>reach: return False
        reach=max(reach,i+n)
    return True

def jump(nums):
    jumps=cur=far=0
    for i in range(len(nums)-1):
        far=max(far,i+nums[i])
        if i==cur: jumps+=1;cur=far
    return jumps

def gas_station(gas,cost):
    if sum(gas)<sum(cost): return -1
    tank=start=0
    for i in range(len(gas)):
        tank+=gas[i]-cost[i]
        if tank<0: tank=0;start=i+1
    return start

def partition_labels(s):
    last={c:i for i,c in enumerate(s)}
    res=[];st=end=0
    for i,c in enumerate(s):
        end=max(end,last[c])
        if i==end: res.append(end-st+1);st=i+1
    return res

if __name__=="__main__":
    print("Can Jump [2,3,1,1,4]:", can_jump([2,3,1,1,4]))
    print("Min Jumps [2,3,1,1,4]:", jump([2,3,1,1,4]))
    print("Gas Station:", gas_station([1,2,3,4,5],[3,4,5,1,2]))
    print("Partition Labels:", partition_labels("ababcbacadefegdehijhklij"))
