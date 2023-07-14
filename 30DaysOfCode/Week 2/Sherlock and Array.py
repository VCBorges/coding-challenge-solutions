# #Non scalable
# def balancedSums(arr):
#     for i in range(len(arr)):
#         before = arr[:i]
#         after = arr[i + 1:]
#         sum_before = sum(before)
#         sum_after = sum(after)

#         if sum_before == sum_after:
#             return 'YES'
#         else:
#             return 'NO'


def balancedSums(arr):
    after = sum(arr)
    before = 0
    for num in arr:
        after -= num
        if before == after:
            return 'YES'
        before += num
    return 'NO'



T = int(input().strip())

for T_itr in range(T):
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = balancedSums(arr)


