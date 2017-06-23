# 1000 digit fibonacci number  --dynamic programming   --my best code ever

from time import time


f = {1:1,2:1}

def fib(n):
    if n in f:
        return f[n]
    else:
        f[n] = fib(n - 1) + fib (n - 2)

    return f[n]

def digit_check(n):
    l = str(fib(n))
    if len(l) >= 1000:
        return True
    return False

start = time()
num = 1
while not digit_check(num):
    num += 1
end = time() - start
print(num,end)
