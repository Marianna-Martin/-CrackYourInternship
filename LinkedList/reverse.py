class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev=None
        current =head
        while current:
            next=current.next
            current.next=prev
            prev=current
            current=next
        head=prev
        return head
