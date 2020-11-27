class Solution:
    def reverseWords(self, s: str) -> str:
        retStr= ''
        x = s.split()
        for words in x:
            retStr += words[::-1] + ' '

        return retStr.strip()
