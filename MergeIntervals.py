def merge(intervals):
    intervals.sort(key = lambda interval: interval[0])
    i = 0
    ans = []

    for interval in intervals:
        if not ans or ans[-1][1] < interval[0]:
            ans.append(interval)
        else:
            ans[-1] = ([ans[-1][0], max(ans[-1][1], interval[1])])

    return ans