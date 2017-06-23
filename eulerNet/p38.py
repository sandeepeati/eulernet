

def checkNum(n):
    letters = '123456789'
    for i in letters:
        if i not in n:
            return False
    return True


def concatProduct(n):
    l = len(str(n))
    concProd = ''
    i = 2
    maxN = 0
    while i <= 9:
        for j in range(1,i + 1):
            concProd += str(n * j)
        if checkNum(concProd):
            if int(concProd) > maxN and len(concProd) == 9:
                maxN = int(concProd)
        i += 1
        concProd = ''

    return maxN

maxNum = 0
for i in range(1000000):
    x = concatProduct(i)
    if x > maxNum:
        maxNum = x

print(maxNum)



