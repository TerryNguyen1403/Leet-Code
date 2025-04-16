from typing import List

#Sorted solution
#Time: O(N*log(N))
class Solution1:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if k > len(nums): return 0

        nums.sort()
        i = 1

        while i <= k:
            if i == k:
                return nums.pop()
            nums.pop()
            i += 1
