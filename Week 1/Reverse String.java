class Solution {
    public void reverseString(char[] s) {
        /*Run through the array with two pointers,
        one on each end. Swap on each step till the 
        pointers reach the middle of the array */
        for(int i=0, j=s.length-1; i<j; i++, j--){
            char temp = s[i];
            s[i]=s[j];
            s[j]=temp;
        }
    }
}
