from collections import Counter


class Solution:
    def is_anagram_with_counter(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        c1 = Counter(s)
        c2 = Counter(t)

        return c1 == c2

    def is_anagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s, t = s.lower(), t.lower()

        s, t = (
            s.replace(' ', ''),
            t.replace(' ', ''),
        )

        counts = {}
        for ch in s:
            counts[ch] = counts.get(ch, 0) + 1

        for ch in t:
            n = counts.get(ch, None)
            if n is None:
                return False

            if n == 1:
                del counts[ch]

            else:
                counts[ch] = n - 1

        return not counts
