

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


prime_sieve = {x:x for x in range(1,1000000) if is_prime(x)}
prime_sieve_list = [x for x in range(1,1000000) if is_prime(x)]

longest_chain = 0
ans = 0

for i in prime_sieve_list:
    sumP = i # 2
    chain = 0 # 0
    print(sumP) # 2
    for j in prime_sieve_list:
        if j > i:

            sumP += j # 2 + 3
            chain += 1 # 0 + 1

            if sumP in prime_sieve and chain > longest_chain:
                longest_chain = chain
                ans = sumP


print(ans, longest_chain)
