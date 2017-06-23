# sum of diagonals in a n grid square

n = 1001
sum_of_diagonal = 1
i = 2
while i <= n:
    if i % 2 == 0:
        a = (i * i) + 1
    else:
        a = (i*i)

    sum_of_diagonal += a
    i += 1

for i in range(2,n+1):
    sum_of_diagonal += ((i*(i - 1)) + 1)

print(sum_of_diagonal)
