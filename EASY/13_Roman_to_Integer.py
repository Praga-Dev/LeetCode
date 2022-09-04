class Solution:
    def romanToInt(self, s: str) -> int:
        val_map = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        if len(s) == 0:
            return 0
        val = val_map[s[-1]]
        for i in range(0,len(s)-1):
            v = val_map[s[i]]
            if v < val_map[s[i+1]]:
                val -= v
            else:
                val += v
        return val