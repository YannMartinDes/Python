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

a = int(input("a : "))
b = int(input("b : "))
n = int(input("n : "))

print(expMod(a,b,n))
input()
