ans = pow(2,1000)
ans_str = str(ans)
sumNum = 0
for i in range(0,len(ans_str)):
    t = int(ans_str[i])
    sumNum += t


print(sumNum)
