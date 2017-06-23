# largest palindrome made from the product of two 3-digit numbers

def ispalindrome(n):
    y = str(n)
    rev = int(y[::-1])
    if n == rev:
        return True
    return False

minNum = 100
maxNum = 999
maxAns = 10000
for i in range(maxNum,minNum - 1,-1):
    for j in range(maxNum,minNum - 1,-1):
        p = i * j
        if maxAns < p and ispalindrome(p):
            maxAns = p

print(maxAns)
