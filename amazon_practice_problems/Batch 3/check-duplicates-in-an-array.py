class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        """ I'm going to leverage the fact that each number that appears in the array 'nums'
        is less than or equal to the value of the length of the array.
        This in-place solution involves modifying the current element at the index corresponding to
        each value within the array and adding x (which here is the length of the array) to it
        So any element that appears more than once will result in that index having a final
        in-place value of more than 2 times the length of the array. Hence we'll know which number
        has apperared twice """

        for i in nums:
            nums[i%len(nums)] = nums[i%len(nums)] + len(nums)

        retArr=[]
        for j in range(len(nums)):
            if nums[j] > (len(nums)*2):
                if j==0:
                    retArr.append(len(nums))
                else:
                    retArr.append(j)

        return retArr

        
