from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l_arr = [0] * n
        r_arr = [0] * n
        l_mult = 1
        r_mult = 1

        for i,j in zip(range(0,n), range(n-1,-1,-1)):
            l_arr[i] = l_mult
            r_arr[j] = r_mult
            l_mult *= nums[i]
            r_mult *= nums[j]

        result = [0] * n

        for i in range(len(l_arr)):
            result[i] = l_arr[i] * r_arr[i]

        return result

    #Space optimal
    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product = 1
        right_product = 1
        result = [0] * n

        for i in range(0,n):
            result[i] = left_product
            left_product *= nums[i]

        for j in range(n-1,-1,-1):
            result[j] *= right_product
            right_product *= nums[j]

        return result
