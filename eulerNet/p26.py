#  maximum recurring digits (did not solved) --look later
a = {}

for i in range(1,1001):
    t = str(1 / i)[2:]
    a[i] = t

max = 0
maxNum = 0

for j in range(1,1001):
    c = 0
    for d in a[j]:
        if d == a[j][0] and d != 0:
            n = c
        c += 1
    if c > max:
        max = c
        maxNum = j

print(a[983])
