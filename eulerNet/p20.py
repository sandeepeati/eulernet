# factorial -pretty easy

def fact(n):
    if n == 1:
        return 1
    return n * fact(n-1)

fact_100 = str(fact(100))

sum_of_number = 0
for i in fact_100:
    sum_of_number += int(i)

print(sum_of_number)
