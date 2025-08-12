from collections import Counter


def is_anagram(s1: str, s2: str) -> bool:
    if len(s1) != len(s2):
        return False

    c1 = Counter(s1)
    c2 = Counter(s2)

    return c1 == c2
