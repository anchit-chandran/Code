import random
import timeit


def insertion_sort(nums):
    for step in range(1, len(nums)):
        key = nums[step]
        j = step - 1

        while j >= 0 and (key < nums[j]):
            nums[j + 1] = nums[j]
            j -= 1

        nums[j + 1] = key

    return nums


nums = [1, 5, 9, 4, 3]
# print(insertion_sort(nums))


def merge(lst1, lst2):
    p1, p2 = 0, 0
    res = []
    while (p1 < len(lst1)) and (p2 < len(lst2)):
        if lst1[p1] <= lst2[p2]:
            res.append(lst1[p1])
            p1 += 1
        else:
            res.append(lst2[p2])
            p2 += 1

    if p1 < len(lst1):
        res.extend(lst1[p1:])
    else:
        res.extend(lst2[p2:])

    return res


def merge_sort(nums):
    if len(nums) == 1:
        return nums

    mid = len(nums) // 2
    first_half = merge_sort(nums[:mid])
    second_half = merge_sort(nums[mid:])

    return merge(first_half, second_half)


nums = [
    68,
    30,
    3,
    19,
    4,
    79,
    27,
    18,
    98,
    39,
    13,
    36,
    65,
    94,
    46,
    70,
    78,
    0,
    0,
    50,
    81,
    26,
    87,
    65,
    92,
    75,
    99,
    74,
    97,
    90,
    86,
    14,
    52,
    56,
    66,
    4,
    10,
    70,
    39,
    43,
    90,
    57,
    14,
    8,
    82,
    33,
    25,
    72,
    34,
    0,
    29,
    58,
    45,
    63,
    54,
    54,
    68,
    83,
    48,
    11,
    6,
    24,
    55,
    87,
    17,
    51,
    9,
    87,
    33,
    74,
    49,
    88,
    56,
    28,
    92,
    43,
    76,
    68,
    59,
    90,
    12,
    24,
    47,
    2,
    1,
    25,
    80,
    33,
    43,
    7,
    19,
    95,
    95,
    29,
    73,
    74,
    97,
    95,
    21,
    39,
]
sorting_algorithms = [insertion_sort, merge_sort, sorted]

for algo in sorting_algorithms:
    def runner():
        algo(nums)
    avg_time = timeit.timeit(runner, number=50) / 50
    print(f'{algo} avg time: {avg_time}')
