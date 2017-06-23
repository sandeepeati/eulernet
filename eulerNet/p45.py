from time import time


start = time()

triangular_numbers = [(((x*x)+x)//2) for x in range(60000)]

pentagonal_numbers = [1]

i = 2
p = 1
while p <= 1533776805:
    p = ((3 * i * i) - i) // 2
    if p in triangular_numbers:
        pentagonal_numbers.append(p)
    i += 1


hexagonal_numbers = []

j = 2
while len(hexagonal_numbers) <= 1:
    h = ((2*j*j) - j)
    if h in pentagonal_numbers:
        hexagonal_numbers.append(h)
    j += 1
end = time() - start
print(hexagonal_numbers[-1],'%d'% end)



