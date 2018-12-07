import time
from random import randint

zero = 0
um = 0

def fast_power(base, power):
    """
    Returns the result of a^b i.e. a**b
    We assume that a >= 1 and b >= 0
    Remember two things!
     - Divide power by 2 and multiply base to itself (if the power is even)
     - Decrement power by 1 to make it even and then follow the first step
    """
    result = 1
    while power > 0:
        # If power is even
        if power % 2 == 0:
            # Divide the power by 2
            power = power / 2
            # Multiply base to itself
            base = base * base
        else:
            # Decrement the power by 1 and make it even
            power = power - 1
            # Take care of the extra value that we took out
            # We will store it directly in result
            result = result * base

            # Now power is even, so we can follow our previous procedure
            power = power / 2
            base = base * base

    return result


def ePrimo(p):

    if p < 50:
        x = randint(2,p-1)
    else: 
        x = 2#randint(2,p-1)

    print(x)
    aux = (fast_power(x, p)) % p
    aux = aux - x
    print(aux)
    if aux == 0:
        return 0
    else:
        return 1


a = int(input())

start_time = time.time()

b = ePrimo(a)

print("--- %s seconds ---" % (time.time() - start_time))
if b == 0:
    print("PRIMO")
else:
    print("COMPOSTO")


