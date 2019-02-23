import time
from random import randint

def ePrimo(p):

    if p < 50:
        x = 2#randint(2,p-1)
    else: 
        x = 2#randint(2,p-1)

    #print(x)
    var  = 1
    aux = x
    rest =1
    i = 1
    while (i < p-1):
        
        aux = aux * x    
        #print("Aux:%s"%aux)                     
        if aux >= p and rest ==1:
            rest = aux%p
            s = (p-1-i)//(i+1)
            if (rest > 1 or s > 1) :
                aux = rest
                continue
            print("Rest:%s"%rest)
            aux = 1
            
            print("S:%s"%s)
            var = rest**(s+1)
            
            fim = (p-1-i)%(i+1)
            print("Fim:%s"%(p-1-i))
            i = p-1-fim
            continue
        i = i+1
        
    aux = ( aux * var)%p
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
#for i in range (1):
b = ePrimo(a)
 #   if b == 0:
  #      zero+=1
   # else:
    #    um+=1
print("--- %s seconds ---" % (time.time() - start_time))
if b==0:
    print("PRIMO")
else:
    print("COMPOSTO")

#POTENCIA E MODULO POR PARTES


