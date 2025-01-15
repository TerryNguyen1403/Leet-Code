class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True

        my_stack = []
        my_dict = {')': '(',
                   ']': '[',
                   '}': '{'}

        #(])
        for c in s:
            if c in my_dict.values():
                my_stack.append(c)
            elif c in my_dict:
                if not my_stack or my_dict.get(c) != my_stack[-1]:
                    return False
                my_stack.pop()



        return True if len(my_stack) == 0 else False
