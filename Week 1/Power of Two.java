class Solution {
    public boolean isPowerOfTwo(int n) {
        /*Bitwise operation can be used on this problem
        since powers of two have only the MSB as 1 and the
        rest as 0s. The number right before the power of two
        will have one less bit and 1s in all it's bits so
        an & operation will give 0 if the number is a power of
        two. */
        return (n>0 && ((n & n-1) ==0));
    }
}
