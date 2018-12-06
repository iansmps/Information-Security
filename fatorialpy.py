import sys 
import time
 
def binomial(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke.
    See http://stackoverflow.com/questions/3025162/statistics-combinations-in-python
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0

def primetest(n):
    head = n//2
    print(head)
    while(head!=1):
        a = binomial(n,head)
        #print(a)
        if a % n != 0:
            return 0
        else:
            head = head - 1
    return 1




a = int(input("Número: "))
start_time = time.time()
b = primetest(a)
print("--- %s seconds ---" % (time.time() - start_time))
if b == 0:
    print("COMPOSTO")
else:
    print("PRIMO") 

#OTIMIZAR OPERAÇÕES