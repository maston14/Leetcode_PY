# Origin
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        n = float(n)
        while n > 1:
            n = n / 3
        return n == 1

# 1 line solution
class Solution2(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        # 1162261467 is 3^19,  3^20 is bigger than int  
        return n > 0 and 1162261467 % n == 0