def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)-1
        okindex=n
        for i in range(n,-1,-1):
            if i+nums[i]>=okindex:
                okindex=i
        if okindex==0:
            return True
        else:
            return False

