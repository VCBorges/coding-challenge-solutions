class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        if len(strs) == 1:
            return [strs]

        hash = {}
        for i, v in enumerate(strs):
            sorted_str = ''.join(sorted(v))
            if hash.get(sorted_str, None):
                hash[sorted_str].append(v)
            else:
                hash[sorted_str] = [v]

        return list(hash.values())
