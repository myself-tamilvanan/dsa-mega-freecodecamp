"""LC 853 - Car Fleet"""
def car_fleet(target, position, speed):
    pairs = sorted(zip(position, speed), reverse=True)
    stack = []
    for pos, spd in pairs:
        time = (target - pos) / spd
        if not stack or time > stack[-1]:
            stack.append(time)  # new fleet
        # else: merges with fleet ahead
    return len(stack)

if __name__ == "__main__":
    cases = [
        (12,[10,8,0,5,3],[2,4,1,1,3],3),
        (10,[3],[3],1),
        (100,[0,2,4],[4,2,1],1),
    ]
    for target,pos,spd,expected in cases:
        result = car_fleet(target,pos,spd)
        print(f"target={target}, pos={pos}, spd={spd} -> {result} fleets {'✓' if result==expected else '✗'}")
