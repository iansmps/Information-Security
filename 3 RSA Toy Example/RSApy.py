import random
import sys
import math
import time
from random import randrange

def ehPrimo(a):
    prime = 0
    nprime = 0
    for i in range (11):
        r = random.randrange(2, a-1)
        b = modexp(r,a,a) - r
        if b == 0:
            prime+=1
        else:
            nprime+=1
    

    if prime > nprime:
        return True
    else:
        return False

def generateLargePrime(k):

     r = 100*(math.log(k,2)+1) 
     r_ = r
     while r>0:

         n = random.randrange(2**(k-1),2**(k))
         r -= 1
         if ehPrimo(n) == True:
             return n

     return "Failure"

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def inv_multi(a, b):
    x = 0
    y = 1
    lx = 1
    ly = 0
    oa = a 
    ob = b  
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lx) = ((lx - (q * x)), x)
        (y, ly) = ((ly - (q * y)), y)
    if lx < 0:
        lx += ob  
    if ly < 0:
        ly += oa  
    return lx

def generate_keypair(keySize=56):
    p=1
    q=1
    while(p==q):
        p = generateLargePrime(keySize)
        q = generateLargePrime(keySize)

    n = p*q
    phi = (p-1)*(q-1)

    e = random.randrange(1, phi)

    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    d = inv_multi(e, phi)

    return ((e, n), (d, n))

def encrypt(pk, plaintext):

    key, n = pk

    cipher = [modexp(ord(char),key,n) for char in plaintext]

    return cipher

def decrypt(pk, ciphertext):

    key, n = pk

    plain = [chr(modexp(char,key,n)) for char in ciphertext]

    return ''.join(plain)

def modexp ( r, u, p ):

   s = 1
   while u != 0:
      if u & 1:
         s = (s * r)%p
      u >>= 1
      r = (r * r)%p
   return s


#print("\nGerando chaves\n")
#public, private = generate_keypair()
#print("Chave Pública: ", public ,"\nChave Privada: ", private)
chave = (920923141140617518756575559310317, 2303212569848295598518260591436383)
message = [int(x) for x in input("\nInsira a mensagem criptografada:").split()]

#encrypted_msg = encrypt(public, message)

#print("\nA mensagem criptografada é:")
#print(encrypted_msg)

print("\nA mensagem descriptografada é:")
print(decrypt(chave, message))
print("\n")