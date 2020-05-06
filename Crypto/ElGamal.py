"""
p premier
a générateur

clef privé = k < p
clef publique = B = a**k % p
^ (p, a, B)
"""

"""
Chiffrement ElGamal:
r random
c1 = a**r % p
c2 = M*B**r % p
C = (c1, c2)
"""

"""
Dechiffrement ElGamal:
C = (c1, c2)
M = (c2 * c1**-k) % p
"""

import math
import random

# Ca trouve aussi les coeff
def bezout (a,b):
    if b == 0 :
        return (a,1,0)
    q = a // b
    r=a%b
    (g,u1,v1) = bezout(b,r)
    return (g,v1,u1-q*v1)

#Calcul de Beta
def B(a,k,p):
    return a**k%p

#Encrypt
def E (M, a, p, B, r):
    #r = random.randint(1, 1000)
    c1 = a**r % p
    c2 = M*B**r % p
    return (c1, c2)

#Inverse
def Inv(c1,k,p):
    return bezout((c1**k)%p, p)

#Decrypt
def D (c1, c2, k, p):
    (_, pp, _) = Inv(c1,k,p)
    M = (c2 * pp) % p 
    return M

