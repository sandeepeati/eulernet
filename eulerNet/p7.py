# 10001st prime number

def isprime(n):
    c = 0
    for i in range(1,n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    return False


primes = []
i = 1
while len(primes) <= 10000:
    if isprime(i):
        print(len(primes))
        primes.append(i)
    i += 1

print(primes[-1])
