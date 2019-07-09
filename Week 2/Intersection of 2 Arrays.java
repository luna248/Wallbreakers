class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        //Find the length of the smallest string
        int l = (nums1.length < nums2.length) ? nums1.length : nums2.length;

        //Convert the larger array into a hashset
        Set<Integer> set = new HashSet<Integer>();
        for (int i : (nums1.length > nums2.length) ? nums1 : nums2)
        {
            set.add(i);
        }

        //Create a set to keep track of all the intersections. This will be converted
        //to an int array at the end since that is the return type.
        Set<Integer> intnums = new HashSet<Integer>();

        //Parse the smaller array and check if each element exists in the other array or not
        int[] smaller = (nums1.length < nums2.length) ? nums1 : nums2;
        for(int i=0; i<l; i++){
            if(set.contains(smaller[i]) && !intnums.contains(smaller[i])){
                intnums.add(smaller[i]);
            }
        }

        //Convert back to an int[]
        return intnums.stream().mapToInt(Integer::intValue).toArray();
    }
}
