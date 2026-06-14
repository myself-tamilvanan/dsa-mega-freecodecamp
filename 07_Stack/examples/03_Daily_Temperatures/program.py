"""LC 739 - Daily Temperatures"""
def daily_temperatures(temps):
    res = [0]*len(temps)
    stack = []  # indices
    for i,t in enumerate(temps):
        while stack and temps[stack[-1]] < t:
            j = stack.pop()
            res[j] = i-j
        stack.append(i)
    return res
if __name__=="__main__":
    cases=[[73,74,75,71,69,72,76,73],[30,40,50,60],[30,60,90]]
    for t in cases:
        print(f"{t}\n-> {daily_temperatures(t)}")
