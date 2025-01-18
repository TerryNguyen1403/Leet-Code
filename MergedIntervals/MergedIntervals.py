from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals)
        res = [sorted_intervals[0]]
        index = 0

        for i in range(1,len(sorted_intervals)):
            if res[index][1] >= sorted_intervals[i][0]:
                res[index][1] = max(res[index][1],sorted_intervals[i][1])
            else:
                index += 1
                res.append(sorted_intervals[i])

        return res
        #Time: O(N*Log(N))
        #Space: O(1)
