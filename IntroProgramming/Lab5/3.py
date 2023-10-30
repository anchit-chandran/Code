import itertools

def targetSum(nums, target):
    nums.sort()
    combos = list(itertools.combinations(nums, 4))
    res = []
    for combo in combos:
        if (sum(combo) == target) and (combo not in res):
            res.append(combo)
    return res

print(targetSum([3, 0, -1, 0, -2, 5], 2))