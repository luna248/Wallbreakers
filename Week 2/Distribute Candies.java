class Solution {
    public int distributeCandies(int[] candies) {
        //Create a hashset to keep track of all the unique candies
        Set<Integer> unique = new HashSet<>();
        for (int i : candies){
            unique.add(i);
        }

        return Math.min(candies.length / 2, unique.size());
    }
}
