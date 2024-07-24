class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        r1=nums[0]*nums[1]*nums[2]
        r2=nums[-1]*nums[-2]*nums[0]
        if r1>r2:
            return r1
        else:
            return r2
