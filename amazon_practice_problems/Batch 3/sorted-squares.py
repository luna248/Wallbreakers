class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        squares=sorted([pow(i,2) for i in A])
        return squares
