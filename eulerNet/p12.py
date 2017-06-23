# first triangular number to have over five hundred divisors
import math

def factors(n):
    number_of_factors = 0
    for i in range(1, int(math.ceil(math.sqrt(n)))):
        if n % i == 0:
            number_of_factors +=2
        if i*i==n:
            number_of_factors -=1
    return number_of_factors

x=1
for y in range(2,1000000):
    x += y
    if factors(x) >= 500:
        print(x)
        break
