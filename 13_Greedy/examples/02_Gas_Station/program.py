"""LC 134 - Gas Station"""
def can_complete_circuit(gas, cost):
    if sum(gas) < sum(cost): return -1
    tank = start = 0
    for i in range(len(gas)):
        tank += gas[i] - cost[i]
        if tank < 0:
            tank = 0
            start = i + 1
    return start

if __name__ == "__main__":
    cases = [
        ([1,2,3,4,5],[3,4,5,1,2]),
        ([2,3,4],[3,4,3]),
        ([5,1,2,3,4],[4,4,1,5,1]),
    ]
    for gas, cost in cases:
        print(f"gas={gas}, cost={cost} -> start at index {can_complete_circuit(gas,cost)}")
