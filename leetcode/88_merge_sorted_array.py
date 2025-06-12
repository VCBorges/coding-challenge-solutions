class Solution:
    def merge(
        self,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int,
    ) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_relevant_part = nums1[:m]
        sorted_result = sorted(nums1_relevant_part + nums2)
        for i in range(len(nums1)):
            nums1[i] = sorted_result[i]



[1].