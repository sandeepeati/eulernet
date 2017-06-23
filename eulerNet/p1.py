# sum of multiples of 3 and 5 below 1000

n = 1000
s = 0
for i in range(1,1000):
    if i % 3 == 0 or i % 5 == 0:
        print(i)
        s += i

print(s)
