class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        evenNums= []
        oddNums= []
        result= []
        for i in A:
            if i%2==0:
                evenNums.append(i)
            else:
                oddNums.append(i)

        count=0
        while(count<len(evenNums)):
            result.append(evenNums[count])
            result.append(oddNums[count])
            count+=1

        return result
