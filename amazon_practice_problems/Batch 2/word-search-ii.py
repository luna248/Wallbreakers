class Solution:
    def searchGrid(self, board, word, i, j):
        if not word:
            return True

        if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or board[i][j]!=word[0]:
            return False

        char= board[i][j]
        board[i][j]= '#'
        checkAdj = ( self.searchGrid(board, word[1:], i+1, j) or
                     self.searchGrid(board, word[1:], i, j+1) or
                     self.searchGrid(board, word[1:], i-1, j) or
                     self.searchGrid(board, word[1:], i, j-1) )
        board[i][j]= char
        return checkAdj

    def wordFound(self, board, word):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.searchGrid(board, word, i, j):
                    return True
        return False

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        wordsFound= []
        for word in words:
            if self.wordFound(board, word):
                wordsFound.append(word)
        return wordsFound
