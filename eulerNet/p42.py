
def name_value(name):
    s = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    value = 0
    for i in name:
        value += (s.index(i) + 1)

    return value


triangle_numbers = [(((n * n) + n) // 2) for n in range(1,10000)]

count = 0

with open('p42.txt') as f:
    names = f.readline()
f.close()

names = names.split('","')
names[0] = 'A'
names[-1] = 'YOUTH'

for i in names:
    x = name_value(i)
    if x in triangle_numbers:
        count += 1

print(count)
