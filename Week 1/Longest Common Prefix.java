class Solution {
    public String longestCommonPrefix(String[] strs) {
        boolean check=true;
        int j=0; int i;
        char c;
        int length= strs[0].length();
        while (check){
            c= strs[0].charAt(j);
            for(i=1; i<strs.length && j<strs[i].length(); i++){
                if(strs[i].charAt(j)!=c){
                    check=false;
                    break;
                }

            else{
                j++;
            }
            }
        }
        return strs[0].substring(0,j-1);
    }
}
