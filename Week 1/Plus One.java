class Solution {
    public int[] plusOne(int[] digits) {
        int l = digits.length-1;

        /* If the last digit is less than 9, adding 1
        will not impact the rest of the number. */
        if(digits[l]!=9)
        {
            digits[l] += 1;
            return digits;
        }

        /*But if it is 9, we need to consider the entire number
        and various other test cases as well. Such as all nines
        in the number which will increase the final array length */
        else
        {
            /*The array is looped through to find all the 9s
            and the pointer is stopped right before the first
            digit in case it contains all nines */
            while(digits[l]==9 && l>0)
            {
                digits[l]=0;
                l=l-1;
            }

            /*If the first digit is a nine, then a new array is
            created with length 1 greater than the original length
            and the first digit one followed by all zeros */
            if(digits[l]==9)
            {
                int[] d2 = new int[digits.length+1];
                d2[0]=1;
                return d2;
            }
            /*Else the digit is just incremented by one as it doesn't
            impact the rest of the number */
            else
            {
                digits[l] += 1;
                return digits;
            }
        }
    }
}
