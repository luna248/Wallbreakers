class Solution {
    public int[] twoSum(int[] nums, int target) {
        int checkFor;
        for(int i=0; i<nums.length; i++){
            checkFor = target - nums[i];
            for(int j=i+1; j<nums.length;j++){
                if(nums[j]==checkFor){
                    int[] A = {i,j};
                    return A;
                }
            }
        }
        int[] A = {0,0};
        return A;
    }
}
