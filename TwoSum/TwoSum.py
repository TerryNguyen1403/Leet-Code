from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for index, num in enumerate(nums):
            if target - num not in my_dict:
                my_dict[num] = my_dict.get(num, index)
            else:
                return [my_dict[target - num], index]