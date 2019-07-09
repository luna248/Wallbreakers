public static void main(String args[]){
  public static patternDescription( String pattern, String Description){
    /* Create a map between each character of the pattern and the word it's
    supposed to be mapped with. For every occurence of the pattern, match the
    character with the word, and if it's different, return false */

    //Split the words in description into a string array but using split() and a space delimiter
    char[] descWords = Description.split(" ");

    //Test case #1
    if(pattern.length()!= descWords.length){
      return false;
    }

    //Initialize a HashMap
    Map<Character, String> charMap = new HashMap<Character, String>();

    for(int i=0; i<pattern.length(); i++){
      if(!charMap.containsKey(pattern.charAt(i)))
      {
        charMap.put(pattern.charAt(i), descWords[i]);
      }
      else if(charMap.get(pattern.charAt(i)) != descWords[i])
      {
        return false;
      }
    }

    return true;
  }
}
