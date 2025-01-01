class Solution:
    #Stack solution
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack = []

        for c in s:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()

        s = ''.join(stack)

        while stack:
            stack.pop()

        for c in t:
            if c != '#':
                stack.append(c)
            elif stack:
                stack.pop()

        t = ''.join(stack)

        return s == t
    # Time: O(n+m)
    # Space: O(n+m)

    # While loop with Space: O(1)
    def backspaceCompare2(self, s: str, t: str) -> bool:
        i = len(s) - 1
        j = len(t) - 1

        skipS = 0
        skipT = 0

        while i >= 0 or j >= 0:
            while i >= 0:
                if s[i] == '#':
                    skipS += 1
                    i -= 1
                elif skipS > 0:
                    skipS -= 1
                    i -= 1
                else:
                    break

            while j >= 0:
                if t[j] == '#':
                    skipT += 1
                    j -= 1
                elif skipT > 0:
                    skipT -= 1
                    j -= 1
                else:
                    break

            if i >= 0 and j >= 0 and s[i] != t[j]:
                return False

            if (i >= 0) != (j >= 0):
                return False

            i -= 1
            j -= 1

        return True
        #Time: O(n+m)
        #Space: O(1)