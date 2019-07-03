class Solution {
    public int uniqueMorseRepresentations(String[] words) {
        //Morse string
        String[] morse = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        //Create counter for alphabets
        int j=97;

        //Initialize a new hashmap and create a map of alphabets and their appropriate
        //morse code.
        Map<Character,String> a2m = new HashMap<Character, String>();
        for(int i=0; i<morse.length; i++){
            a2m.put((char)j, morse[i]);
            j++;
        }

        //Create a hashset to keep track of unique morse code concatenations
        Set<String> set = new HashSet<String>();

        //Use Stringbuilder to build the morse translation
        StringBuilder sb = new StringBuilder("");

        //Build a morse string out of each word and add unique ones to the hashset
        for(int i=0; i<words.length; i++){
            sb.setLength(0);
            for(int k=0; k<words[i].length(); k++){
               sb.append(a2m.get(words[i].charAt(k)));
            }
            if(!set.contains(sb.toString())){
                set.add(sb.toString());
            }
        }

        //return the size of the hashset
        return set.size();
    }
}
