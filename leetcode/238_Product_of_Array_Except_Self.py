class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        prefix = [1] * n
        prefix[0] = nums[0]
        for i in range(1, n):
            prefix[i] = nums[i] * prefix[i - 1]

        postfix = [1] * n
        postfix[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            postfix[i] = postfix[i + 1] * nums[i]

        answer = [1] * n
        for i in range(n):
            if i == 0:
                answer[i] = postfix[i + 1]

            elif i == (n - 1):
                answer[i] = prefix[i - 1]

            else:
                answer[i] = prefix[i - 1] * postfix[i + 1]

        return answer
