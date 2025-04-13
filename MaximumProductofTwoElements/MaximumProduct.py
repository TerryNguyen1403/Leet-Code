from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first_value, second_value = float('-inf'), float('-inf')
        index = 0

        while (index < 2):
            if index == 0:
                for i in range(len(nums)):
                    if nums[i] > first_value:
                        first_value = nums[i]
                nums.remove(first_value)
                index += 1
            else:
                for i in range(len(nums)):
                    if nums[i] > second_value:
                        second_value = nums[i]
                nums.remove(second_value)
                index += 1

        return (first_value - 1) * (second_value - 1)
