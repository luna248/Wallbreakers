class Solution {
    public boolean isHappy(int n) {
        //Create a hashset to keep track of all the square sums
        Set<Integer> set = new HashSet<Integer>();

        //Create a loop to call the square sum method till the sum is 1
        //Add each result to the hashset, if the number has already been noted before
        //then return false
        while(n!=1){
            n=squareSum(n);
            if(set.contains(n)){
                return false;
            } else {
                set.add(n);
            }
        };
        return true;
    }

    //The following function sums up the square of each digit in the number
    public int squareSum(int n){
        int sum=0;
        while(n>0){
            sum += Math.pow(n%10, 2);
            n=n/10;
        }
        return sum;
    }
}
