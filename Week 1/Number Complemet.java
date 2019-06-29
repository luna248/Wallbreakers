class Solution {
    public int findComplement(int num) {
        //Calculate the total number of bits in the number
        int numbits =  (int)(Math.floor(Math.log(num) / Math.log(2))) + 1;

        //Use XOR with the original number and the left shifted bit total
        //to get the complement
        return ((1 << numbits) - 1) ^ num;
    }
}
