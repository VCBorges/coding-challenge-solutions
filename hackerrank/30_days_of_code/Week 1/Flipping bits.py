import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#


def flippingBits(n):
    # Write your code here
    result = 0
    for i in range(31, -1, -1):
        if n // (2**i) == 1:
            n = n - 2**i
            x = 0
        else:
            x = 1
        result += 2**i * x

    return result


q = int(input().strip())

for q_itr in range(q):
    n = int(input().strip())

    result = flippingBits(n)

    print(result)
