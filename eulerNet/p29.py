

ans_list = []

for a in range(2,101):
    for b in range(2,101):
        ans = pow(a,b)
        if ans not in ans_list:
            ans_list.append(ans)


print(len(ans_list))
