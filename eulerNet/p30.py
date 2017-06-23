def check(n,p):
    if n == 1 or n == 0:
        return False
    else:
        n = str(n)
        sum = 0
        for i in range(len(n)):
            sum += pow(int(n[i]),p)
        if sum == int(n):
            return True
        return False

listNum = []

for i in range(354295):
    if check(i,5):
        listNum.append(i)

print(sum(listNum))
