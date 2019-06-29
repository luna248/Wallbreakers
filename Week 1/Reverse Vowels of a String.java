class Solution {
    public String reverseVowels(String s) {
        /*Lookup table has been created using a hashset to
        check if a given character is a vowel or not. Test
        cases have been considered and capital letters have
        been added to the lookup table as well */
        HashSet<Character> h = new HashSet<Character>();
        h.add('A');
        h.add('a');
        h.add('E');
        h.add('e');
        h.add('I');
        h.add('i');
        h.add('O');
        h.add('o');
        h.add('U');
        h.add('u');

        char[] ch = s.toCharArray();

        /*Using two pointers, one on each side of the word
        parse the String till a vowel is found from both
        sides and swap when it has been*/
        for(int i=0,j=ch.length-1; i<j; i++,j--){
            while(!h.contains(ch[i]) && i<j){i++;}
            while(!h.contains(ch[j]) && i<j){j--;}
            char temp = ch[i];
            ch[i] = ch[j];
            ch[j] = temp;
        }

        return String.copyValueOf(ch);
    }
}
