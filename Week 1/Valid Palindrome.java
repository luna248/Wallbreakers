class Solution {
    public boolean isPalindrome(String s) {
        //Test Case
        if(s.isEmpty()){
            return true;
        }

        /*To keep the operations simple, the entire string is converted to
        lower case.
        The isLetterOrDigit() function has been used to eliminate spaces
        and other special characters from consideration.
        Two pointers on each end are run through the string and the letters
        are matched to determine whether it's a palindrome or not */
        s= s.toLowerCase();
        for(int i=0,j=s.length()-1; i<j; i++,j--){
            while(!Character.isLetterOrDigit(s.charAt(i)) && i<j){ i++; }
            while(!Character.isLetterOrDigit(s.charAt(j)) && j>i){ j--; }
            if(s.charAt(i)!=s.charAt(j)){
                return false;
            }
        }
        return true;
    }
}
