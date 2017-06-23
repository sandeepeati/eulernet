# problem statement:
# n --> n/2(if n is even)
# n --> 3n + 1(if n is odd)
# ex: 13 --> 40 --> 20 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1
# chain contains 10 terms so answer is 10

# This sequnce is known as COLLATZ PROBLEM, it is thought that all starting numbers
# finish at 1

# which starting number, under one million, produces the longest chain

num = 1000000

def collatz(n):
    arr = [n]
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1

        arr.append(n)

    return len(arr)

maxChain = 0
ansNum = 0
while num > 0:
    length = collatz(num)
    if length > maxChain:
        maxChain = length
        ansNum = num
        print(maxChain,ansNum,'\n')
    num -= 1

print(maxChain, ansNum)



