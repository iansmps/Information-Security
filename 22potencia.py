import time
from random import randint

def pot(p):
    b = 2
    listpot = [2]
    a = 2
    start_time = time.time()
    while b <= p/2:
        b = b*2
        a = a * a
        listpot.append(a)
    #print(listpot)
    print("1--- %s seconds ---" % (time.time() - start_time))
    start_time = time.time()
    primo = p
    res = 1
    #p = p-b
    while p != 0:
        b = b//2
        #tam = len(listpot)
        fat = listpot.pop()
        #print(fat)

        while p >= b:
            res = res*fat
            p = p - b
    print("2--- %s seconds ---" % (time.time() - start_time))
    res = (res % primo) - 2
    return res
            

        
a = int(input())

print (pot(a))
