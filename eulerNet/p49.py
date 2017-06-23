import itertools

def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

primes_sieve = {x:x for x in range(1000,10000) if is_prime(x)}

def perm(x,y,z):
    x = str(x)
    y = str(y)
    z = str(z)
    perm = list(map("".join, itertools.permutations(x)))

    if x in perm and y in perm and z in perm:
        return True
    return False


for c in range(1000,10000):
    for d in range(1,5001):
        if c in primes_sieve:
            x = perm(c - (2 * d), c - d, c)
            if c - d in primes_sieve and c - (2 * d) in primes_sieve and x:
                s = str(c - (2 * d)) + str(c - d) + str(c)
                print(s)

