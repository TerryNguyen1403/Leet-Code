class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        characters = [0] * 26

        for c in ransomNote:
            characters[ord(c) - ord('a')] += 1

        for c in magazine:
            characters[ord(c) - ord('a')] -= 1

        for value in characters:
            if value > 0:
                return False

        return True

    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        chars = {}

        for c in magazine:
            chars[c] = chars.get(c,0) + 1

        for c in ransomNote:
            if c not in chars:
                return False
            elif chars.get(c) == 1:
                del chars[c]
            else:
                chars[c] -= 1

        return True