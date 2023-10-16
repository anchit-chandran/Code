nums = [1,2,3]

for ix, num in enumerate(nums):
    print(f'{ix} - {num}')

outcomes = [True, True, True, False]
print(any(outcomes), all(outcomes))