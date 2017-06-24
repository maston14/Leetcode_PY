# Origin
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i = len(num1) - 1
        j = len(num2) - 1
        carry = 0
        ret = ""
        while i >= 0 or j >= 0:
            i_val = (int)(num1[i]) if i >= 0 else 0
            j_val = (int)(num2[j]) if j >= 0 else 0
            sum = i_val + j_val + carry
            bit = sum % 10
            carry = (int)(sum / 10)

            ret = str(bit) + ret
            i -= 1
            j -= 1
        if carry > 0:
            ret = str(carry) + ret

        return ret