class Solution {
    public int[] sortArrayByParity(int[] A) {
        int start=0;
        int end=A.length-1;

        while(start<end){

            if(A[start]%2==1 && A[end]%2==0){
                //Integer on the left is odd and the right is even
                swap(A, start, end);
                start++;
                end--;
            }
            else if(A[start]%2==1 && A[end]%2==1){
                //Integer on the left and right are both odd
                end--;
            }
            else{
                //Integer on the left is even
                start++;
            }

        }

        return A;
    }


    public int[] swap(int[] A, int i, int j){
        int temp = A[i];
        A[i] = A[j];
        A[j] = temp;
        return A;
    }
}
