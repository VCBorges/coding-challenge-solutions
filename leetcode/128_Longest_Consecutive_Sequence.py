class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        if not nums:
            return 0

        if len(nums) == 1:
            return 1

        nums = sorted(list(set(nums)))
        seq = 1
        longest = 1
        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] == 1:
                seq += 1
                if i == len(nums) - 1:
                    if seq > longest:
                        longest = seq

            else:
                if seq > longest:
                    longest = seq
                seq = 1

        return longest

    def longestConsecutive_alternative(self, nums: list[int]) -> int:
        seen = set(nums) 
        longest = 0

        for num in seen: 
            if num - 1 not in seen:
                length = 1
                cur = num + 1
                while cur in seen:  # walk the consecutive run
                    length += 1
                    cur += 1
                longest = max(longest, length)

        return longest
