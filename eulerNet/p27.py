# equation that produces maximum chain of prime numbers for a  consecutive numbers
#  submitted in eqn starting from 0

def prime(n):
    y = n//2
    c = 0
    if n == 1:
        return False
    else:
        for i in range(1,y+1):
            if n % i == 0:
                c += 1
    if c == 1:
        return True
    return False

primes_1000 = [x for x in range(1005,1,-1) if prime(x)]
primes_5000 = {x:x for x in range(5001) if prime(x)}

maxChain = 0
product = 1

for b in primes_1000:
    for a in range(-b,b):
        n = 1
        eqn = b

        while (eqn in primes_5000):
            eqn = ((n * n) + (a*n) + b)
            n+=1

        if n > maxChain:
            maxChain = n
            product = a * b

print(maxChain, product)

