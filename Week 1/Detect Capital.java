class Solution {
    public boolean detectCapitalUse(String word) {
        /*Initialize counters to keep track of all the
        uppercase and lowercase numbers*/
        int upperNum =0;
        int lowerNum =0;

        /*Convert String to character array and check if each
        letter is uppercase or lowercase*/
        for(char c: word.toCharArray()){
            if(Character.isUpperCase(c)){
                upperNum++;
            }
            else{
                lowerNum++;
            }
        }

        /*If the entire word is uppercase or lowercase, it is acceptable. It is also okay if the first letter is uppercase and the rest
        is lowercase, but every other case should return a false */
        if(upperNum==word.length() || lowerNum==word.length() || (Character.isUpperCase(word.charAt(0)) && lowerNum==word.length()-1)){
            return true;
        } else{
            return false;
        }
    }
}
