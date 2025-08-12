class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join((char for char in s if char.isalnum())).lower()
        if not s:
            return True

        n = len(s)
        start, end = 0, (n - 1)
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1

        return True
