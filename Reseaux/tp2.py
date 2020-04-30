import math
import random
import matplotlib.pyplot as plt
import tp1


def make_T(A=1.5, Fo=750.0, fe=8000.0, ph=0, N=32, kmax = 2*7):
    #3.1.1
    te = 1.0/fe
    d = N * fe
    
    sig_t = []
    sig_n = []
    sig_s = []
    sig_an = []
    sig_bn = []
    
    for i in range(N):
        t = te*i
        k = 0
        sig_t.append(t)
        sig_n.append(i)
        sig_bn.append(bnT())
        sig_an.append(anT(i,A))
    
        res = 0
        while k <= kmax :
            res += anT(k,A)* math.cos(2*math.pi*k*Fo*t + ph)
            k += 1

        sig_s.append(res)
        
        
    return sig_t,sig_n, sig_s, sig_an, sig_bn

def anT(k,A):
    if(k%2 == 1):
        return ((8*A) / (math.pow(math.pi,2) * math.pow(k,2)))
    return 0 

def bnT():
    return 0

def make_R(A=1.5, Fo=750.0, fe=8000.0, ph=0, N=32, kmax = 2*7):
    #3.1.1
    te = 1.0/fe
    d = N * fe
    
    sig_t = []
    sig_n = []
    sig_s = []
    sig_an = []
    sig_bn = []
    
    for i in range(N):
        t = te*i
        k = 0
        sig_t.append(t)
        sig_n.append(i)
        sig_bn.append(bnR(i,A))
        sig_an.append(anR())
    
        res = 0
        while k <= kmax :
            res += bnR(k,A)* math.sin(2*math.pi*k*Fo*t + ph)
            k += 1

        sig_s.append(res)
        
        
    return sig_t, sig_n, sig_s, sig_an, sig_bn

def anR():
    return 0 

def bnR(k,A):
    if(k == 0): return 0
    return (-1 * ((2*A) / (math.pi * k)))

def make_C(A=3, Fo=750.0, fe=8000.0, ph=0, N=32, kmax = 2*7):
    #3.1.1
    te = 1.0/fe
    d = N * fe
    
    sig_t = []
    sig_n = []
    sig_s = []
    sig_an = []
    sig_bn = []
    
    for i in range(N):
        t = te*i
        k = 0
        sig_t.append(t)
        sig_n.append(i)
        sig_bn.append(bnC(i,A))
        sig_an.append(anC())
    
        res = 0
        while k <= kmax :
            res += bnC(k,A)* math.sin(2*math.pi*k*Fo*t + ph)
            k += 1

        sig_s.append(res)
        
    return sig_t, sig_n, sig_s, sig_an, sig_bn

def anC():
    return 0 

def bnC(k,A):
    if(k%2 == 1):
        return ((2*A) / (math.pi * k))
    return 0

def make_three_cos(A=1,fe=1000.0, N=256):
    """
    Create a synthetic 'sine wave'
    """
    te = 1.0/fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te*i
        sig_t.append(t)
        sig_s.append(0)
        sig_s[i] += (A*math.cos(2*math.pi*10*t))
        sig_s[i] += (A*math.cos(2*math.pi*20*t))
        sig_s[i] += (A*math.cos(2*math.pi*400*t))
        
    return sig_t, sig_s

h = [-6.849167e-003, 1.949014e-003, 1.309874e-002,1.100677e-002,\
            -6.661435e-003,-1.321869e-002, 6.819504e-003, 2.292400e-002,7.732160e-004,\
            -3.153488e-002,-1.384843e-002,4.054618e-002,3.841148e-002,-4.790497e-002,\
            -8.973017e-002, 5.285565e-002,3.126515e-001, 4.454146e-001,3.126515e-001,\
            5.285565e-002,-8.973017e-002,-4.790497e-002, 3.841148e-002, 4.054618e-002,\
            -1.384843e-002,-3.153488e-002, 7.732160e-004,2.292400e-002,6.819504e-003,\
            -1.321869e-002,-6.661435e-003, 1.100677e-002,1.309874e-002,1.949014e-003,\
            -6.849167e-003]

def convolution(A,fe,N):
    x,y = make_three_cos(1,1000,256)

    y2 = []
    for i in range(N):
        y2.append(0)
        for k in range(len(h)):
            if(i-k >= 0):
                y2[i] += h[k] * y[i-k]
                #attention ! x correspond au signal c'est donc y ici

    return x,y2

#-----------------------------------------
if __name__ == '__main__':
    """
    ##### SIGNAL T
    fig,ax = plt.subplots(3)
    
    x1,x2,y1,y2,y3 = make_T(3,750.0,8000.0,0,32,200)
    tp1.plot_on_ax(ax[0],x1,y1,"signal T",'b.-')
    tp1.decorate_ax(ax[0],"f = 750, fe = 8000")
    
    tp1.plot_on_ax(ax[1],x2,y2,"an",'go')
    tp1.decorate_ax(ax[1],"")
    
    tp1.plot_on_ax(ax[2],x2,y3,"bn",'go')
    tp1.decorate_ax(ax[2],"")
    
    plt.savefig("./sigT.png")
    plt.show()
    """
    """
    #### SIGNAL R
    fig,ax = plt.subplots(3)
    x1,x2,y1,y2,y3 = make_R(3,750.0,8000.0,0,32,200)
    
    tp1.plot_on_ax(ax[0],x1,y1,"signal R",'b.-')
    tp1.decorate_ax(ax[0],"f = 750, fe = 8000")
    

    tp1.plot_on_ax(ax[1],x2,y2,"an",'go')
    tp1.decorate_ax(ax[1],"")
    
    tp1.plot_on_ax(ax[2],x2,y3,"bn",'go')
    tp1.decorate_ax(ax[2],"")
    
    plt.savefig("./sigR.png")
    plt.show()

    """
    """
    #### SIGNAL C
    fig,ax = plt.subplots(3)
    x1,x2,y1,y2,y3 = make_C(3,750.0,8000.0,0,32,200)
    
    tp1.plot_on_ax(ax[0],x1,y1,"signal C",'b.-')
    tp1.decorate_ax(ax[0],"f = 750, fe = 8000")
    

    tp1.plot_on_ax(ax[1],x2,y2,"an",'go')
    tp1.decorate_ax(ax[1],"")
    
    tp1.plot_on_ax(ax[2],x2,y3,"bn",'go')
    tp1.decorate_ax(ax[2],"")
    
    plt.savefig("./sigC.png")
    plt.show()
    """

    ####### CONVOLUTION
    x,y = make_three_cos(1,1000,256)
    x2,y2 = convolution(1,1000,256)
    fig,ax = plt.subplots(2)

    tp1.plot_on_ax(ax[0],x,y,"3 cosinus avec 10hz 20hz 400hz",'b.-')
    tp1.plot_on_ax(ax[1],x2,y2,"signal filtré",'b.-')

    plt.savefig("./convolution.png")
    plt.show()

    
