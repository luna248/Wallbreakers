class Solution {
    public List<String> fizzBuzz(int n) {
        //Using a new list to hold the new values.
        List<String> finalList= new ArrayList<String>();

        //Parsing each number in the range with a for loop
        for(int i=1; i<=n; i++){
            if(i%3==0 && i%5==0){
                finalList.add("FizzBuzz");
            } else if(i%3==0){
                finalList.add("Fizz");
            } else if(i%5==0 ){
                finalList.add("Buzz");
            } else{
                finalList.add(String.valueOf(i));
            }
        }
    return finalList;
    }
}
