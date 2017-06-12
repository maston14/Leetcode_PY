# Origin
# build a map, add all even and odd - 1; if there is an odd, +1
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        map = {}
        for c in s:
            if c not in map:
                map[c] = 1
            else:
                map[c] += 1

        even = 0
        odd = 0
        flag = 0

        for i in map:
            if map[i] % 2 == 0:
                even += map[i]
            else:
                odd += map[i] - 1
                flag = 1

        return even + odd + flag