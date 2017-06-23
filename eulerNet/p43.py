import itertools

sample = '1234567890'
all_pan = list(map("".join, itertools.permutations(sample)))

def prop(num):
    p1 = int(num[1:4])
    p2 = int(num[2:5])
    p3 = int(num[3:6])
    p4 = int(num[4:7])
    p5 = int(num[5:8])
    p6 = int(num[6:9])
    p7 = int(num[7:])
    if p1 % 2 == 0 and p2 % 3 == 0 and p3 % 5 == 0 \
        and p4 % 7 == 0 and p5 % 11 == 0 and p6 % 13 == 0 \
            and p7 % 17 == 0:
        return True
    return False

ans = 0

for i in all_pan:
    if prop(i):
        ans += int(i)

print(ans)
