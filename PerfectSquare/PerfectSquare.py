class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True

        l,r = 1, num

        while l < r:
            mid = (l+r)//2
            m_squared = mid*mid

            if m_squared == num:
                return True
            elif m_squared > num:
                r = mid
            elif m_squared < num:
                l = mid + 1

        return False
