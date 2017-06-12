# Origin
# use list as a map for each character
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        s_count = [0] * 26
        t_count = [0] * 26

        base = ord('a')

        for i in range(len(s)):
            s_count[ord(s[i]) - base] += 1
            t_count[ord(t[i]) - base] += 1

        return s_count == t_count