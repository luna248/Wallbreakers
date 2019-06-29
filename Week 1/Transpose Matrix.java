class Solution {
    public int[][] transpose(int[][] A) {
        //Get the row and column length of the original matrix
        int rLen= A.length;
        int cLen= A[0].length;

        //Create a new matrix with the lengths exchanged
        //Row lenght in column, column length in row
        int[][] B= new int[cLen][rLen];

        //Run through the original matrix and insert
        //the numbers into swapped x and y coordinates
        //E.g: Element in orig:(1,3) to new:(3,1)
        for(int i=0;i<rLen;i++){
            for(int j=0;j<cLen;j++){
                B[j][i]=A[i][j];
            }
        }
        //return the new matrix
        return B;
    }
}
