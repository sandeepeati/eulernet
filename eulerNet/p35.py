from time import time

start = time()

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



def rot(n):
    num = []
    y = str(n)
    for i in range(len(y)):
        q = n // 10
        r = n % 10
        a = int(str(r) + str(q))
        if a not in num:
            num.append(a)
        n = a
    return num

primes_million = primesList(1000000)
ans = {2:2,3:3,5:5,7:7}

for i in primes_million:
    x = rot(i)
    for j in range(len(x)):
        if x[j] not in primes_million:
            break
    else:
        ans[i] = i

end = time() - start

print(len(ans)," solved in %d seconds" % end)
