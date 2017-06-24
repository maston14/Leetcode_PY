# Origin
# use xor
class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret = 0
        for i in range(len(nums) + 1):
            ret ^= i
        for i in nums:
            ret ^= i
        return ret

# use sum
class Solution2(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        return n * (n+1)/2 - sum(nums)

# binary search, if sorted, it is best
class Solution3(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        left = 0
        right = len(nums)
        while left < right:
            mid = (int) ((left + right) / 2)
            if mid < nums[mid]:
                right = mid
            else:
                left = mid + 1
        return left

a = [0,2,3]
test = Solution3()
print(test.missingNumber(a))