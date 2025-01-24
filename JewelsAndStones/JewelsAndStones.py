class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        hash_map = {}
        for c in jewels:
            hash_map[c] = hash_map.get(c,0) + 1

        count = 0

        for c in stones:
            if c in hash_map:
                count += 1

        return count