class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length() != t.length()){
            return false;
        }

        Set<Character> set = new HashSet<Character>();
        for(int i=0; i<s.length(); i++){
            set.add(s.charAt(i));
        }

        for(int i=0; i<t.length(); i++){
            if(!set.contains(t.charAt(i))){
                return false;
            }
        }

        return true;
    }
}
