from typing import List

class Solution:
    #Iterative solution
    #Time: O(Log(n)
    #Space: O(1)
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1 and nums[0] == target: return 0

        left,right = 0, len(nums) - 1

        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1

        return -1

    #Recursive solution
    # Time: O(Log(n)
    # Space: O(Log(n))
    def search2(self, nums: List[int], target: int)->int:
        if len(nums) == 1 and nums[0] == target: return 0
        def recursion(left: int, right: int) -> int:
            if left > right: return -1
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                return recursion(left,mid-1)
            else:
                return recursion(mid+1,right)

        return recursion(0,len(nums)-1)
