from typing import List

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        intersection = {}
        result = []

        for num in nums1:
            if num in intersection:
                intersection[num] += 1
            else:
                intersection[num] = 1

        for num in nums2:
            if num in intersection and intersection.get(num) > 0:
                result.append(num)
                intersection[num] -= 1

        return result

    #Time: O(n + m)

