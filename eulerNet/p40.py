

num = ''
while len(num) <= 1000000:
    for i in range(1,1000000):
        num += str(i)


print(int(num[0]) * int(num[9]) * int(num[99]) * int(num[999]) * int(num[9999]) * int(num[99999]))
