class Solution {
    public int singleNumber(int[] nums) {
        //Any number XORed with itself will give zero,
        //so if we are to find the unique number in the array
        //we XOR all the numbers and the one that remains (doesn't
        //cancel out) is the unique number
        int unique = 0;
        for(int i=0; i<nums.length; i++){
            unique = unique ^ nums[i];
        }
        return unique;
    }
}
