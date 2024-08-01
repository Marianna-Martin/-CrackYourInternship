//Multiply two numbers represented by Linked Lists
class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        head1=first
        head2=second
        res1=0
        res2=0
        while head1:
            res1=res1*10+head1.data
            head1=head1.next
        while head2:
            res2=res2*10+head2.data
            head2=head2.next
        return res1*res2
            
