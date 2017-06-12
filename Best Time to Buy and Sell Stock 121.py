# Origin
# Scan and record the min, every time check the min and max
import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minP = sys.maxsize
        maxD = 0
        for i in prices:
            minP = min(minP, i)
            maxD = max(maxD, i - minP)
        return maxD
