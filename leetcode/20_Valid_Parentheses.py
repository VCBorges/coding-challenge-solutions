class Solution:
    def isValid(self, s: str) -> bool:
        left = {'(': 1, '{': 2, '[': 3}
        right = {')': 1, '}': 2, ']': 3}
        stack = []

        for i in s:
            if i in left:
                stack.append(i)
            else:
                if len(stack) == 0:
                    return False

                if left[stack.pop()] != right[i]:
                    return False

        return len(stack) == 0
