class Solution {
    public List<Integer> selfDividingNumbers(int left, int right) {
        /* Create a new array that will hold all the self dividing
        numbers in the range */
        ArrayList<Integer> finalList= new ArrayList<Integer>();
        for(int i=left; i<=right; i++){
            if(isSelfDividing(i)){
                finalList.add(i);
            }
        }
        return finalList;
    }

    public boolean isSelfDividing(int i){
        //Using a temp to get all the digits in the numbers
        int iCopy = i;
        int j;

        //Checking if each digit is a divisor
        while(iCopy>0){
            j = iCopy%10;
            if(j==0){
                return false;
            }
            else if(i%j==0){
                iCopy=iCopy/10;
            }
            else{
                return false;
            }
        }
        return true;
    }
}
