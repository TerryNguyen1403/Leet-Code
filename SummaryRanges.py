from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        n = len(nums)
        i = 0
        result = []

        while i < n:
            start = nums[i]

            while i < n - 1 and nums[i] + 1 == nums[i+1]:
                i += 1

            if start != nums[i]:
                result.append(str(start) + '->' + str(nums[i]))
            else:
                result.append(str(start))

            i += 1

        return result
