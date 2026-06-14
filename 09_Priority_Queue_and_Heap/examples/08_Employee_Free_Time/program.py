"""LC 759 - Employee Free Time"""
def employee_free_time(schedule):
    # Flatten all intervals
    all_intervals = []
    for employee in schedule:
        for interval in employee:
            all_intervals.append(interval)
    # Sort by start
    all_intervals.sort(key=lambda x: x[0])
    # Merge overlapping
    merged = [all_intervals[0][:]]
    for start, end in all_intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])
    # Find gaps
    free = []
    for i in range(1, len(merged)):
        free.append([merged[i-1][1], merged[i][0]])
    return free

if __name__ == "__main__":
    cases = [
        [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]],
        [[[1,3],[6,7]],[[2,4]]],
        [[[1,2],[2,3]],[[3,4],[4,5]]],
    ]
    for schedule in cases:
        print(f"Schedule: {schedule}")
        print(f"  Free time: {employee_free_time(schedule)}")
