class Solution:
    def isAnagram(self,s: str, t: str) -> bool:
        #Base case
        if len(s) < len(t): return False

        my_dict = {}

        for c in s:
            my_dict[c] = my_dict.get(c,0) + 1

        for c in t:
            if c not in my_dict:
                return False
            elif my_dict[c] == 1:
                del my_dict[c]
            else:
                my_dict[c] -= 1

        return True