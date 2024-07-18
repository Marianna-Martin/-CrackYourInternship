def moveZeroes(self, nums):

        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        c=0
        j=0
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
              c=c+1
            else:
              nums[j]=nums[i]
              j=j+1
        nums[j:n]=[0]*c
        return nums
