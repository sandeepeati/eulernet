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


def panDigi(n):
    letters = '123456789'
    if len(str(n)) > 9:
        return False
    else:
        for i in letters[:len(str(n))]:
            if str(n).count(i) != 1:
                return False
        else:
            return True

panDigNum = []

for i in range(3,10000000):
    if panDigi(i):
        panDigNum.append(i)

ans = 0

for j in range(len(panDigNum)-1,0,-1):
    if is_prime(panDigNum[j]):
        print(panDigNum[j])
        break

end = time() - start

print(end)
