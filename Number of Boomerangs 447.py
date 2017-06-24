# Origin
# for every node, compute every pair. SUPER SLOW
class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for point in points:
            distance_map = {}
            for iter in points:
                if iter != point:
                    dist = self.squareDistance(point, iter)
                    if dist not in distance_map:
                        distance_map[dist] = []
                    distance_map[dist].append(iter)

            for k in distance_map:
                n = len(distance_map[k])
                if n >= 2:
                    ans += self.factorial(n) / self.factorial(n - 2)

        return ans

    def squareDistance(self, a, b):
        return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2

    def factorial(self, n):
        ans = 1
        for i in range(1, n + 1):
            ans *= i
        return ans