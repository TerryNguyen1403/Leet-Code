from typing import List

class Solution:
    # Using array
    def firstUniqChar(self, s: str) -> int:
        freq = [0] * 26

        for c in s:
            freq[ord(c) - ord('a')] += 1

        for index, char in enumerate(s):
            if freq[ord(char) - ord('a')] == 1:
                return index

        return -1
        #Time: O(N)
        # Space: O(1)

    # Using Hashmap
    def firstUniqChar2(self, s: str) -> int:
        freq = {}

        for char in s:
            freq[char] = freq.get(char, 0) + 1

        for index,char in enumerate(s):
            if freq[char] == 1:
                return index

        return -1
        #Space: O(N)
        #Time: O(N)