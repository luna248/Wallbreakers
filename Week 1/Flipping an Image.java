class Solution {
    public int[][] flipAndInvertImage(int[][] A) {
        //Get the length of each row
        int j=A.length-1;

        //Parse each row from the top of the 2D array and
        //run through the array with pointers on each end
        //gradually moving towards the middle.
        //Swap on each step
        for(int k=0; k<A.length;k++){
            for(int i=0; i<A.length;i++){

                //Swap on each step till the middle of the
                //row is reached
                if(j-i>i){
                    swap(A,k,i,j-i);
                }

                //Invert each bit as you go through the row.
                if(A[k][i]==0){
                    A[k][i]=1;
                } else{
                    A[k][i]=0;
                }
            }
        }
        return A;
    }

    public int[][] swap(int[][] A, int k, int i, int j){
        int temp= A[k][i];
        A[k][i]=A[k][j];
        A[k][j]=temp;

        return A;
    }
}
