# sum of even valued terms in fibonacci series starting from
# 1 and 2 till four million

a = 1
b = 2
s = 0

while b < 4000000:
    if b % 2 == 0:
        s += b

    c = a + b
    a = b
    b = c

print(s)
