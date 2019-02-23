
from random import randint
import time

def power(x,p):
    if p>1000000000000000:
        i = 1000000
    else: 
        if p> 100000000:
            i = 100000
        else:
            i = 10000
    div = p//i
    res = (pow(x,int(div)))%p
    res = pow(res,i)*pow(x,(p%i))%p
    return res - x

def modexp ( g, u, p ):
   s = 1
   while u != 0:
      if u & 1:
         s = (s * g)%p
      u >>= 1
      g = (g * g)%p
   return s


a = int(input("Número: "))
test = 0
start_time = time.time()

b = modexp(5424534,a,a) - 5424534
print(b)

print("--- %s seconds ---" % (time.time() - start_time))

if b == 0:
    print("PRIMO")
else:
    print("COMPOSTO")   