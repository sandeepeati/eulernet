from time import time

start = time()

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

primes_sieve = {x:x for x in range(1,1000000) if is_prime(x)}

def factors(n):
    facs = {}
    for i in range(1,(n//2)+1):
        if n%i == 0:
            facs[i] = i

    return facs

def p47(n):
    i = 0
    numCount = []
    while i <= 3:
        count = 0
        num = n + i
        fac = factors(num)
        for j in fac:
            if j in primes_sieve:
                count += 1
        numCount.append(count)
        i += 1

    for k in numCount:
        if not k >= 4:
            return False
    else:
        return True

for l in range(210,200000):
    print(l)
    if l not in primes_sieve:
        if p47(l) == True:
            print(l,"ans found")
            break

end = time() - start

print("%d"%end)
