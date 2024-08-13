class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if 0 in nums1[m:m+n]:
            x=nums1.index(0,m,m+n)
            nums1[x:m+n]=nums2[0:n]
        else:
            nums1+=nums2
        nums1=nums1.sort()


