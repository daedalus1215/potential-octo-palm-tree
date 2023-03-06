class Solution:
    def __init__(self):
        self.symbols = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}

    def romanToInt(self, s: str) -> int:
        """
        :param s: the roman numerals. eg: IV = 4
        :return:
        """
        new = s.replace("IV", "IIII").replace("IX", "VIIII").replace("XL", "XXXX").replace(
            "XC", "LXXXX"
        ).replace("CD", "CCCC").replace("CM", "DCCCC")
        return sum(map(lambda x: self.symbols[x], list(new)))


assert Solution().romanToInt(s="IV") == 4
assert Solution().romanToInt(s="III") == 3
assert Solution().romanToInt(s="LVIII") == 58
assert Solution().romanToInt(s="MCMXCIV") == 1994
