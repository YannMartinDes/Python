def bezout(a,b) : # retourne (g,u,v) avec g = pgcd(a,b)
    if b == 0 : # et tel que g = a*u + b*v
        return (a,1,0)
    x = 1
    y = 0
    xPrime = 0
    yPrime = 1
    
    while b>0 :
        q = a // b # r = a - b.q
        r = a % b
        xSeconde = x - q * xPrime
        ySeconde = y - q * yPrime
        a = b
        b = r
        x = xPrime
        y = yPrime
        xPrime = xSeconde
        yPrime = ySeconde

    return (a,x,y)

def clef_priv(e,m):
    pgcd,u,v = bezout(m,e)
    return v

def clef_pub(L,e,m):
    return [(e*i)%m for i in L]

def chiffre(M,clef_pub):
    res = 0
    for i in range(len(M)) :
        res += int(M[i]) * clef_pub[i]
    return res

def dechiffre(C,d,m):
    return (d * C)% m
