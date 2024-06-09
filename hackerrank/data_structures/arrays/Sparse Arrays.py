def matching_strings(
    string_list: list[str],
    queries: list[str],
) -> list[int]:
    result = [0 for _ in range(len(queries))]
    for i in range(len(queries)):
        for j in range(len(string_list)):
            if queries[i] == string_list[j]:
                result[i] += 1
    return result


if __name__ == '__main__':
    stringList_count = int(input().strip())

    stringList = []

    for _ in range(stringList_count):
        stringList_item = input()
        stringList.append(stringList_item)

    queries_count = int(input().strip())

    queries = []

    for _ in range(queries_count):
        queries_item = input()
        queries.append(queries_item)

    res = matching_strings(stringList, queries)
