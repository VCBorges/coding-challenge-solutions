def countTriplets(arr: list[int], r: int) -> int:
    """
    - Find the count of distinct triplets of indexes from arr
    that form a G.P. with ratio r

    r = 2
    arr = 1 2 2 4
          |

    triplets = 2 ((0,1,3), (0,2,3))

    frequency = {4: 1, 2: 2, 1: 1}
    pairs = {2: 2}
    triplets = 2
    """
    triplets = 0
    frequency = {}
    pairs = {}

    for n in reversed(arr):
        if n * r in pairs:
            triplets += pairs[n * r]

        if n * r in frequency:
            pairs[n] = pairs.get(n, 0) + frequency[r * n]

        frequency[n] = frequency.get(n, 0) + 1

    return triplets
