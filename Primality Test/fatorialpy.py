import sys 
import time
 
def binomial(n, k):
    if 0 <= k <= n:
        naux = 1
        kaux = 1
        for t in range(1, min(k, n - k) + 1):
            naux *= n
            kaux *= t
            n -= 1
        return naux // kaux
    else:
        return 0

def primetest(n):
    head = 3
    limit = 1000
    #print(limit)

    while(head!=limit and head!=(n//2)+1):
        a = binomial(n,head)
        #print(a)
        if a % n != 0:
            return 1
        else:
            head = head + 1
    return 0


a = int(input("Número: "))

start_time = time.time()
b = primetest(a)
print("--- %s seconds ---" % (time.time() - start_time))

if b == 1:
    print("COMPOSTO")
else:
    print("PRIMO") 

