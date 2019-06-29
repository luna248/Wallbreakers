class Solution {
    public String reverseWords(String s) {
        int start=0;
        int end=0;

        /* Convert string to character array to
        perform retrieval operations more efficiently */
        char[] ch= s.toCharArray();

        /* Everytime a space is found in the string,
        swap the entire word that comes before it. To swap letters
        in the last word, I have created a separate condition just
        to address that test case */
        for(int i=0; i<ch.length; i++){
            if(ch[i]== ' '){
                end=i-1;
                swap(ch, start, end);
                start = i+1;
            } else if(i==ch.length-1){
                end=i;
                swap(ch, start, end);
            }
        }
        return String.copyValueOf(ch);
    }

    /* The swap logic works the same way as in the "Reverse String" 
    submission */
    public void swap(char[] ch, int start, int end){
        for(int i=start, j=end; i<j; i++, j--){
            char temp = ch[i];
            ch[i] = ch[j];
            ch[j] = temp;
        }
    }
}
