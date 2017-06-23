
def fact(n):
    if n == 1 or n == 0:
        return 1
    return n * fact(n - 1)

def magic_func(n):
    y = str(n)
    sum = 0
    for i in range(len(y)):
        sum += fact(int(y[i]))

    if sum == n:
        return True
    return False

numSum = 0

for i in range(10,40586):
    if magic_func(i):
        numSum += i
        print(i,'\n')

print(numSum)


