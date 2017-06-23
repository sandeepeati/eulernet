# smallest positive number that is evenly divisible by all
# of the numbers from 1 to 20

def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

l = 2
for i in range(3,21):
    l = lcm(l,i)

print(l)


