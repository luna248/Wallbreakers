class Solution:
    def foundBattleship(self, board, i, j) -> bool:
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='X':
            return False

        board[i][j]= '#'
        self.foundBattleship(board, i+1, j)
        self.foundBattleship(board, i, j+1)
        self.foundBattleship(board, i-1, j)
        self.foundBattleship(board, i, j-1)
        return True

    def countBattleships(self, board: List[List[str]]) -> int:
        totalBattleships= 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.foundBattleship(board, i, j):
                    totalBattleships += 1
        return totalBattleships
