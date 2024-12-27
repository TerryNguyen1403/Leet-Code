from typing import List

class Solution:
    def intersection(self,nums1: List[int], nums2: List[int]) -> List[int]:
        intersection_arr = []
        result = []

        for num in nums1:
            if num not in intersection_arr:
                intersection_arr.append(num)

        for num in nums2:
            if num in intersection_arr:
                result.append(num)
                intersection_arr.remove(num)

        return result