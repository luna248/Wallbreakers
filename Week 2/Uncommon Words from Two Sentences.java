class Solution {
    public String[] uncommonFromSentences(String A, String B) {
        //Since we're checking words in both the strings, it's better to combine them
        //and then perform operations on one string
        String ab = A + " " + B;
        String[] allWords = ab.split(" ");

        //Create a hashmap to keep count of how many times each word appears
        Map<String, Integer> wordCount = new HashMap<String, Integer>();
        for(int i=0; i<allWords.length; i++){
            if(wordCount.containsKey(allWords[i])){
                wordCount.put( allWords[i], wordCount.get(allWords[i]) + 1);
            } else{
                wordCount.put (allWords[i],1);
            }
        }

        //Create a String List for unique words
        List<String> uncommonWords = new ArrayList<>();

        //Iterate through the Hashmap to get all words with the count 1
        for(String key:wordCount.keySet())
            if(wordCount.get(key) == 1)
                uncommonWords.add(key);

        //Conver the List to string array and return
        return uncommonWords.toArray(new String[uncommonWords.size()]);
    }
}
