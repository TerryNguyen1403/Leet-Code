from collections import defaultdict

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        words = defaultdict(int)
        count = float('-inf')

        for c in text:
            if c in 'balloon':
                words[c] += 1

        count = min(words['b'],words['a'],words['l']//2,words['o']//2,words['n'])

        return count
