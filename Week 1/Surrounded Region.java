class Solution {
    public void solve(char[][] board)
    {
        //Edge case
        if (board.length == 0) { return; }

        //Check the border for Os
        for (int i=0; i<board.length; i++)
        {
            BFS(board, i, 0);
            BFS(board, i, board[0].length-1);
        }

        for (int i=0; i<board[0].length; i++)
        {
            BFS(board, 0, i);
            BFS(board, board.length-1, i);
        }
        //NOTE: In this solution, while checking the border nodes, the corners
        //are checked twice, this can be further optimized to avoid that happening.

        for(int i=0; i<board.length; i++)
        {
            for(int j=0; j<board[0].length; j++)
            {
                if(board[i][j] == 'O') { board[i][j]= 'X'; }
                if(board[i][j] == 'S') { board[i][j]= 'O'; }
            }
        }
    }

    public void BFS(char[][] board, int i, int j)
    {
        if((i>=0 && i<board.length)
           && (j>=0 && j<board[0].length)
           && (board[i][j]== 'O'))
           {
                board[i][j]= 'S';
                BFS( board, i-1, j);
                BFS( board, i+1, j);
                BFS( board, i, j-1);
                BFS( board, i, j+1);
           }
    }
}
