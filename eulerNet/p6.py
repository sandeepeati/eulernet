# difference between the sum of the squares of first hundred natural numbers and
# the square of the sum of first hundred natural numbers

sum_n_square = 50 * 50 * 101 * 101

sum = 0
square = 0

for i in range(1,101):
    square = i*i
    print(square)
    sum += square
    print(sum)

print(sum_n_square - sum)
