# Origin
# Basic Idea: DP, 对每一行的每一个都算一下
class Solution(object):
    def minCost(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if costs == []:
            return 0

        for i in range(1, len(costs)):
            for j in range(len(costs[i])):
                opt1 = costs[i - 1][(j + 1) % 3]
                opt2 = costs[i - 1][(j + 2) % 3]
                costs[i][j] += min(opt1, opt2)

        return min(costs[len(costs) - 1])