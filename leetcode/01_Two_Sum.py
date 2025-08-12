class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            if hash.get(nums[i], None) is not None:
                return [hash[nums[i]], i]

            hash[target - nums[i]] = i
