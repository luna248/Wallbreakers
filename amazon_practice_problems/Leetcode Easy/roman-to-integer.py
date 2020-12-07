class Solution:
    def romanToInt(self, s: str) -> int:
        convertMap = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

        prevChar = s[-1]
        intValue = convertMap[prevChar]

        for char in range(len(s)-2, -1, -1):
            if convertMap[s[char]] < convertMap[prevChar]:
                intValue -= convertMap[s[char]]
            else:
                intValue += convertMap[s[char]]
                prevChar = s[char]

        return intValue
