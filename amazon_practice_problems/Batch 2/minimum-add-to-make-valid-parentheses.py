class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        invalid =0
        openParens=0

        for char in S:
            if char=='(':
                openParens+=1
            else:
                if(openParens>0):
                    openParens-=1
                else:
                    invalid+=1

        invalid+=openParens
        return invalid
