
def binary(n):
    rev = ''
    while n > 0:
        r = str(n % 2)
        n = n // 2
        rev += r

    return int(rev[::-1]) == int(rev)

def palindrome(n):
    return str(n) == str(n)[::-1]

sumNum = 0

for i in range(1,1000000):
    if palindrome(i) and binary(i):
        sumNum += i

print(sumNum)
