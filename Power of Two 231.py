# Origin

class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        n = float(n)
        while n > 1:
            n = n / 2
        return n == 1

# Recursive
class Solution2(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n > 0 and ( n == 1 or ( n % 2 == 0 and self.isPowerOfTwo(n / 2) ) )

# bit count
# power of 2, only has one 1 in its binary format
class Solution3(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n > 0 and bin(n).count('1') == 1

# bit
# if n is power of 2, then n & (n-1) is 0
class Solution4(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """

        return n >0 and ( not (n & (n-1)) )