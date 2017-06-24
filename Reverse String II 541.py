# Origin

class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        begin = 0
        ret = ''
        for i in range(0, len(s), 2 * k):
            ret += s[i:i + k][::-1] + s[i + k:i + 2 * k]
        return ret