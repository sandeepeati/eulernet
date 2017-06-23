# Find the sum of all the primes below two million


def sumprime(num):
    def isPrime(n):
        if n == 2:
            return True
        if n == 3:
            return True
        if n % 2 == 0:
            return False
        if n % 3 == 0:
            return False

        i = 5
        w = 2
        while i * i <= n:
            if n % i == 0:
                return False
            i += w
            w = 6 - w
        return True

    if isPrime(num):
        sumP = num - 1
    else:
        sumP = -1

    for x in range(0,num+1):
        if isPrime(x):
            sumP += x

    return sumP


ans = sumprime(2000000)

print(ans)
