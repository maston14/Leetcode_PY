# Origin
class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        ret = ''
        neg = num < 0
        num = abs(num)
        while num != 0:
            bit = num % 7
            num = num / 7
            ret = str(bit) + ret

        if neg:
            ret = '-' + ret
        if ret == '':
            ret = '0'
        return ret

# Better
class Solution2(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'

        ret = ''
        pos = num > 0
        num = abs(num)

        while num != 0:
            ret = str(num % 7) + ret
            num //= 7

        return ret if pos else '-' + ret