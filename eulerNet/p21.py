
# sum of proper divisors of a number

def d(n):
    y = n // 2
    div = [1]
    for i in range(2,y+1):
        if n % i == 0:
            div.append(i)
    sum_of_div = 0
    for i in div:
        sum_of_div += i
    return sum_of_div

a = 0
for i in range(10000):
    if i == d(d(i)) and i != d(i):
        a += i

print(a)
