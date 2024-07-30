class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count=0
        j=1
        for i in range(1,len(nums)):
            if nums[i] in nums[:i]:
                count+=1
            else:
                nums[j]=nums[i]
                j=j+1
        return j 
            
