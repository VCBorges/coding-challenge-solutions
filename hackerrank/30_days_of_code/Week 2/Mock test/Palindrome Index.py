def is_palindrome(s: str) -> bool:
    reversed_string = s[::-1]
    return s == reversed_string


def palindromeIndex(s: str):
    if is_palindrome(s):
        return -1

    n = len(s)

    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            if s[i : n - 1 - i] == s[i : n - 1 - i][::-1]:
                return n - 1 - i
            elif s[i + 1 : n - i] == s[i + 1 : n - i][::-1]:
                return i
    return -1

    # s_list = list(s)
    # for i in range(len(s)):
    #     list_copy = s_list.copy()
    #     list_copy.pop(i)
    #     if is_palindrome(list_copy):
    #         return i

    # return -1


s = 'aaab'

# print(is_palindrome(s))

print(palindromeIndex(s))
