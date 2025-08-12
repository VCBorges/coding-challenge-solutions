class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        n = len(s)
        longest = 1
        substring = 1
        subset = set()
        left, right = 0, 1
        subset.add(s[left])
        while right < n:
            if s[right] not in subset:
                subset.add(s[right])
                right += 1
                substring += 1
                if substring > longest:
                    longest = substring
            else:
                left += 1
                right = left + 1
                subset = set()
                subset.add(s[left])
                substring = 1
        return longest

    def lengthOfLongestSubstring_optimal(self, s: str) -> int:
        char_set = set()
        left = 0
        res = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1
            char_set.add(s[right])
            res = max(res, right - left + 1)
        return res
