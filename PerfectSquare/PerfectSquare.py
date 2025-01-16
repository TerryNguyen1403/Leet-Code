class Solution:
    #Interative solution
    #Time: O(Log(n))
    #Space: O(1)
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

    #Recursion solution
    #Time: O(Log(n))
    #Space: O(Log(n))
    def isPerfectSquare2(self, num: int) -> bool:
        def recursion(l: int,r: int) -> bool:
            if l > r: return False

            mid = (l+r)//2
            mid_square = mid*mid
            if mid_square == num:
                return True
            elif mid_square > num:
                return recursion(l,mid-1)
            elif mid_square < num:
                return recursion(mid+1,r)

        return recursion(1,num)