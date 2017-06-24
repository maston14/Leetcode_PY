# Origin
# count the freq of each element and compare
class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_map = self.freq_count(nums1)
        nums2_map = self.freq_count(nums2)
        ret = []
        for k in nums1_map:
            if k in nums2_map:
                ret += [k] * min(nums1_map[k], nums2_map[k])

        return ret

    def freq_count(self, nums):
        ret_map = {}
        for i in nums:
            if i not in ret_map:
                ret_map[i] = 1
            else:
                ret_map[i] += 1

        return ret_map