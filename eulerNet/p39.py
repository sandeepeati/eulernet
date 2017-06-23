
rt = []

for a in range(1,301):
    for b in range(1,401):
        for c in range(1,501):
            if pow(c,2) == pow(a,2) + pow(b,2) and c > b and b > a:
                p = a + b + c
                if p <= 1000:
                    rt.append(p)


maxCount = 0
maxP = 0

for i in rt:
    if rt.count(i) > maxCount and i != maxP:
        maxCount = rt.count(i)
        maxP = i


print(maxCount, maxP)
