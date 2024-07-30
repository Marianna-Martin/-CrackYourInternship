# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):

        self.val = val
        self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        cn=head
        binary=""
        while cn:
            binary+=str(cn.val)
            cn=cn.next
        return int(binary,2)
