sum_powers = 0

for i in range(1,1001):
    sum_powers += pow(i,i)


ans = str(sum_powers)
start = len(ans) - 10
print(ans[start:])
