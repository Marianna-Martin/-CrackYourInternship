class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None
        """
        # Count occurrences of 0, 1, and 2
        count_0 = nums.count(0)
        count_1 = nums.count(1)
        count_2 = nums.count(2)
        
        # Modify nums in-place
        nums[:count_0] = [0] * count_0
        nums[count_0:count_0 + count_1] = [1] * count_1
        nums[count_0 + count_1:] = [2] * count_2
        return nums
