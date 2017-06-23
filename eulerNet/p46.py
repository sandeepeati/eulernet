from time import time

start = time()

squareList = {(2 * pow(x,2)):(2 * pow(x,2)) for x in range(100000)} # list containing twice the square of a number

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

def check(n):
    checkList = []
    for i in range(1,n):
        if i in primes_sieve:
            twice_square = n - i
            if twice_square in squareList:
                return False
    else:
        return True


for i in range(9,1000000,2):
    if i not in primes_sieve:
        ans = check(i)
        if ans:
           print(i)
           break

end = time() - start
print(end)

