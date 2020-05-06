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

    print("pgcd =",a)
    print("u =",x)
    print("v =",y)
    return (a,x,y)
	
a = int(input("a : "))
b = int(input("b : "))

print(bezout(a,b))
input()
