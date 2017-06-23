# The number 3797 has an interesting property. Being prime itself, it is possible to
# continuously remove digits from left to right, and remain prime at each stage:
# 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right
# and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

from time import time

start = time()

def cutNumLeft(n):
    nums = []
    n = str(n)
    while len(n) > 1:
        n = n[1:]
        nums.append(int(n))

    return nums

def cutNumRight(n):
    nums = []
    n = str(n)
    while len(n) > 1:
        n = n[:-1]
        nums.append(int(n))

    return nums

def primesList(x):
    primeNums = {2:2}
    i = 3
    while i <= x:
        for j in primeNums:
            if not i % j:
                break
        else:
            primeNums[i] = i
        i += 1
    return primeNums


primes_million = primesList(1000000)

sumNum = 0
nums = []
for i in primes_million:
    l = cutNumLeft(i)
    r = cutNumRight(i)
    for x in range(len(l)):
        if l[x] not in primes_million or r[x] not in primes_million:
            break
    else:
        nums.append(i)
        sumNum += i

end = time() - start

print(nums,'\n')
print(sumNum,'\n','runtime is %d'% end)

