# Origin

class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        return list(set_nums1 & set_nums2)


# don't use the intersect of 2 sets
# faster
class Solution2(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret = set()
        set_nums1 = set(nums1)
        for i in nums2:
            if i in set_nums1:
                ret.add(i)

        return list(ret)