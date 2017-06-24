# Origin
# Backtracking
class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        clock = [0] * 10
        ret = set()
        self.helper(ret, clock, num, 0)
        return list(ret)

    def helper(self, ret, clock, led_num, pos):
        if led_num == 0:
            res = self.parseClock(clock)
            if res == None:
                return
            else:
                ret.add(res)
        else:
            for i in range(pos, 10):
                clock[i] = 1
                self.helper(ret, clock, led_num - 1, i + 1)
                clock[i] = 0

    def parseClock(self, clock):
        hour = 0
        minute = 0

        for i in range(0, 4):
            if clock[i] != 0:
                hour += 2 ** (3 - i)
            if hour > 11:
                return None

        for i in range(4, 10):
            if clock[i] != 0:
                minute += 2 ** (5 - (i - 4))
                if minute > 59:
                    return None

        ret = str(hour) + ':'
        if minute < 10:
            ret += '0'
        ret += str(minute)
        return ret