from collections import Counter


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 1:
            return nums

        counter = Counter(nums)
        most_common = counter.most_common(k)
        return [k for k, _ in most_common]
