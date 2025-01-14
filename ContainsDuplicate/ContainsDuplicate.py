from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        freq = {}

        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for num in freq:
            if freq[num] > 1:
                return True

        return False
        #Time: O(N)
        #Space: O(N)

    def containsDuplicate2(self, nums: List[int]) -> bool:
        my_set = set()

        for num in nums:
            if num not in my_set:
                my_set.add(num)
            else:
                return True

        return False
        # Time: O(N)
        # Space: O(N)