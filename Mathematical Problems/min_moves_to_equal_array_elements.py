class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=min(nums)
        sum=0
        new_list = list(map(lambda x: x - m, nums))
        for i in range(len(nums)):
            sum=sum+new_list[i]
        return sum

