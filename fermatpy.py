
from random import randint
import time

def ePrimo(p):

    if p < 50:
        x = randint(2,p-1)
    else: 
        x = 2#randint(2,p-1)

    print(x)
    aux = x
    for i in range (p-1):
        aux = aux * x
        if aux >= p and i != p-2:
            aux = aux%p
    aux = aux - x
    print(aux)
    if aux == 0:
        return 0
    else:
        return 1
""" temp = pow(x,p)-x
    #print(temp)
    
    if temp%p==0:
        return 0
    else: 
        return 1"""

a = int(input())
zero = 0
um = 0
start_time = time.time()
for i in range (1):
    b = ePrimo(a)
    if b == 0:
        zero+=1
    else:
        um+=1
print("--- %s seconds ---" % (time.time() - start_time))
if zero > um:
    print("PRIMO")
else:
    print("COMPOSTO")

#POTENCIA E MODULO POR PARTES