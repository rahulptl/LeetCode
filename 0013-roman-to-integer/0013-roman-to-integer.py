class Solution:
    def romanToInt(self, s: str) -> int:
        
        mapping = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }

        int_value = 0
        prev_val = 0
        for char in reversed(s):

            current_val = mapping[char]
            if current_val < prev_val:
                int_value -= current_val
            else:
                int_value+=current_val
            prev_val = current_val
        return int_value