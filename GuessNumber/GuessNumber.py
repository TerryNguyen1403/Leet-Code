class Solution:
    #Iterative solution
    #Time: O(Log(n)
    #Space: O(1)
    def guessNumber(self, n: int) -> int:
        #picked = 2
        guess = [1,0]
        l,r = 1,n

        while l <= r:
            mid = (l+r)//2
            if guess[mid-1] == -1:
                r = mid
            elif guess[mid-1] == 1:
                l = mid + 1
            else:
                return mid

    #Recursive solution
    # Time: O(Log(n)
    # Space: O(Log(n))
    def guess2(self, n: int)-> int:
        guess = [1,1,1,1,1,0,-1,-1,-1,-1]

        def recursion(left, right):
            mid = (left + right)//2
            last_guess = guess[mid-1]

            if last_guess == 0:
                return mid
            elif last_guess == -1:
                return recursion(left,mid)
            elif last_guess == 1:
                return recursion(mid+1, right)

        return recursion(1,n)