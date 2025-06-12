"""
Determine whether every word in a list appears in another list with at least the
same frequency.

The comparison is **case-sensitive** and duplicate words count:
each occurrence of a word in the first list must be matched by a distinct occurrence
in other list.
"""

from collections import Counter


def checkMagazine(magazine: list[str], note: list[str]) -> None:
    word_counter = Counter(note)
    for word in magazine:
        if word_counter.get(word, None):
            if word_counter[word] > 0:
                word_counter[word] -= 1

    for value in word_counter.values():
        if value > 0:
            print('No')
            return

    print('Yes')
