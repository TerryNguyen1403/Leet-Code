from typing import List

class Solution:
    def romanToInt(self, s: str) -> int:
        my_dict = {
            "I" : 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        my_sum = 0
        my_sum += my_dict.get(s[len(s)-1])

        for i in range(len(s)-2, -1, -1):
            value = my_dict.get(s[i])
            if value < my_dict.get(s[i+1]):
                my_sum -= value
            else:
                my_sum += value

        return my_sum