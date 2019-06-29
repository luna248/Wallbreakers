class Solution {
    public int titleToNumber(String s) {
        int col =0;
        int p = 0;

        /*The column numbers work as a number of base 26, so the int
        value of each alphabet is calculated and multiplied with
        26^(bit position). The total sum of each number gives the
        final value */
        for(int l= s.length()-1; l>=0;l--){
            col += Math.pow(26,p) * (int)(s.charAt(l) - 'A' + 1);
            p++;
        }
        return col;
    }
}
