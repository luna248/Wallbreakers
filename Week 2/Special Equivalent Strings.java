class Solution {
    public int numSpecialEquivGroups(String[] A) {
        //Keep track of number of Special-equivalent groups using a hashmap
        //I'll be using the length of String S from each group and creating an
        //array list with all the special-equivalent words of that length in my hashmap
        Map<Integer, ArrayList<String>> segroup = new HashMap<Integer, ArrayList<String>>();

        //Keep count of total groups
        int groupCount=0;

        for(int i=0; i<A.length; i++)
        {
            String word = A[i];
            //For each word in A, check if a word with the same length exists in the hashmap
            if(!segroup.containsKey(word.length()))
            {
                ArrayList<String> list=new ArrayList<String>();
                list.add(word);
                ++groupCount;
                segroup.put( word.length(), list);
            }
            else
            {
                ArrayList<String> list= segroup.get(word.length());
                boolean check = false;
                int j=0;

                while(!check && j<list.size()){
                    check = areSpecialEquivalent(word, list.get(j));
                    j++;
                }
                if(!check)
                {
                    list.add(word);
                    ++groupCount;
                    segroup.put( word.length(), list);
                }
            }
        }
        System.out.println(segroup);

        return groupCount;
    }

    /*I'll be grouping words together based off the following criteria in this order:
            1. Length
            2. String match
            3. Character match off index(a: 0->length) */
    public boolean areSpecialEquivalent(String S, String T){
        if(S.length()!=T.length()){
            return false;
        }
        else if(S.equals(T))
        {
            return true;
        }
        //If word.length<3 then no swaps are possible
        else if(S.length()<3)
        {
            return false;
        }
        else
        {
            int[] o = new int['z'+1], e = new int['z'+1];
            for(int i=0; i < S.length(); i++){
                if(i % 2 == 0){
                    e[S.charAt(i)]++;
                    e[T.charAt(i)]--;
                }else{
                    o[S.charAt(i)]++;
                    o[T.charAt(i)]--;
                }
            }

            for(int i=0; i < e.length; i++)
                if(e[i] != 0 || o[i] != 0)
                    return false;
            return true;
        }
    }
}
