class Solution:
    def ifLand(self, board: List[List[str]], i, j) -> int:
        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!='1':
            return False

        board[i][j]= '#'
        self.ifLand(board, i+1, j)
        self.ifLand(board, i, j+1)
        self.ifLand(board, i-1, j)
        self.ifLand(board, i, j-1)
        return True

    def numIslands(self, grid: List[List[str]]) -> int:
        totalIslands= 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if self.ifLand(grid, i, j):
                    totalIslands += 1
        return totalIslands
