"""LC 57 - Insert Interval"""
def insert(intervals, new_interval):
    result = []
    i = 0; n = len(intervals)
    # Add all intervals ending before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i]); i += 1
    # Merge all overlapping
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    result.append(new_interval)
    result.extend(intervals[i:])
    return result

if __name__ == "__main__":
    cases = [
        ([[1,3],[6,9]], [2,5]),
        ([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]),
        ([], [5,7]),
        ([[1,5]], [2,3]),
    ]
    for intervals, new in cases:
        print(f"intervals={intervals}, new={new} -> {insert(intervals, new[:])}")
