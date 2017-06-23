# largest prime factor of the number 600851475143


def isprime(n):
    c = 0
    for i in range(1,n + 1):
        if n % i == 0:
            c += 1
    if c == 2:
        return True
    return False


def primes(n):
    n //= 2
    arr = []
    for i in range(0,n + 1):
        if isprime(i):
            arr.append(i)
    return arr

num = 600851475143
reqPrimes = primes(num) # primes below 600851475143

l = len(reqPrimes)
res = [x for x in reqPrimes if num % x == 0]

print(res[-1])
