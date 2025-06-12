class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Remove all ocurrances of val in nums inplace
        # return the number of elements in nums that are not equal to val
        # the first k elements from nums should not not equal to val
        # return k
        original_len = len(nums)
        val_count = nums.count(val)
        for _ in range(val_count):
            nums.remove(val)

        return original_len - val_count

        