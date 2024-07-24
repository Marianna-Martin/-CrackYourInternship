 class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        int_a = int(a, 2)
        int_b = int(b, 2)
        
        # Add the integers
        total = int_a + int_b
        
        # Convert the sum back to binary string
        return bin(total)[2:]
            


