def expMod(a,b,n):
    #print("si trop long utilise pow(a,b,n)")
    repBin = bin(b)[2 : ]
    res = 1

    for c in repBin :
        res = res**2;

        if c == '1' :
            res *= a

        res = res % n
        
    return res;

#Chiffre et Dechiffre du RSA
def e_d(e,d,n):
    while 1:
        choix = input("(e)ncrypt or (d)ecrypt: ")
        nb = int(input("m : "))
                 
        if choix == 'e' :
            print(expMod(nb,e,n))
        else :
            print(expMod(nb,d,n))

e = int(input("e : "))
d = int(input("d : "))
n = int(input("n : "))

e_d(e,d,n)
input()
