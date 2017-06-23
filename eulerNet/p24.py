# permutations below --learn

import itertools

a = [str(x) for x in range(10)]
nums = ["".join(perm) for perm in itertools.permutations(a)]
print(nums[999999])
