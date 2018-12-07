import time
from random import randint

def pot(p):
    b = 2
    listpot = [2]
    a = 2
    while b < p:
        b = b*2
        a = a * a
        listpot.append(a)
    print(listpot)
    #print(listpot[24]**4) 
    b = b/2
    while p != 0:
        p = p-b
        pot = listpot[b]
        


pot(10)