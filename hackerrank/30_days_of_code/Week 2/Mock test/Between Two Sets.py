def first_array_elements_are_all_factors(n: int, arr: list[int]):
    for i in arr:
        if n % i != 0:
            return False
    return True


def is_factor_of_all_elements_in_second_array(n: int, arr: list[int]):
    for i in arr:
        if i % n != 0:
            return False
    return True


def getTotalX(a: list[int], b: list[int]) -> int:
    result = 0
    for i in range(a[0], b[-1] + 1):
        first = first_array_elements_are_all_factors(i, a)
        if first:
            second = is_factor_of_all_elements_in_second_array(i, b)
            if second:
                result += 1
    return result


a = [2, 4]
b = [16, 32, 96]


print(getTotalX(a, b))
