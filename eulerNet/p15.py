def fact(num):
    fac = 1
    while num > 0:
        fac *= num
        num -= 1
    return fac

m = 20
ans = fact(2 * m) // ((fact(m) * fact(m)))
print(ans)
