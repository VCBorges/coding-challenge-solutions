def freqQuery(queries: list[tuple[int, int]]) -> list[int]:
    freq = {}
    result = []
    ds = []

    for query in queries:
        operation = query[0]
        element = query[1]

        if operation == 1:
            ds.append(element)
            freq[element] = freq.get(element, 0) + 1

        elif operation == 2:
            if freq.get(element, 0) > 0:
                ds.remove(element)
                freq[element] -= 1

        elif operation == 3:
            if element in freq.values():
                result.append(1)
            else:
                result.append(0)

    return result
