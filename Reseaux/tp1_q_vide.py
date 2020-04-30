#-*- coding: utf-8 *-*
'''
File tp1_q_vide.py  : Created on 28 feb 2012
@author : menez
Illustration de la quantification
'''
import math
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import tp1

#---------------------------------------------
def QS(sig_s, vmax, b):
    """
    Quantificateur sur b bits d'un signal sig_s
    d'amplitude max vmax.
    Rend le signal quantifie et le bruit sur chaque echantillon.
    """
    # pour l'instant le signal quantifie est le meme que le signal
    # original. Le signal de bruit est donc 0 puisqu'il n'y a pas de
    # quantification.
    res = []
    step = (2*vmax) / (2**b)  #1.25
    minVal = -1/2 * (2**b -1) * step
    steps = [minVal + i * step for i in range(2**b)]
    for e in sig_s:
        if e > 0 : e -= 0.0001
        elif e < 0 : e += 0.0001
        res.append(steps[int((e + vmax)//step)])
    
    return res, [abs(sig_s[i] - res [i]) for i in range(len(res))]

def MSE(sig_s, sig_q, N):
    res = 0
    
    for i in range(len(sig_s)):
        res += (sig_s[i] - sig_q[i])**2
        
    return (1/N)*res
        
def SNR(sig_s, sig_q,N):
    return 10 * math.log((variance(sig_s,N)/MSE(sig_s,sig_q,N)),10)

def variance(sig,N):
    res = 0
    for i in range(len(sig)):
        res += sig[i]**2
    return (1/N) * res

def encodage(sig_s, sig_q,step,b):
    res1 = []
    res2 = []
    res3 = []
    res4 = []
    res5 = []
    
    for i in range(len(sig_s)):
        res1.append(sig_s[i])
        
        res2.append(sig_q[i])
        
        temp = sig_s[i]//step
        res3.append(temp)
        
        if temp >= 0:
            temp = "0"+"{:0{}b}".format(abs(int(temp)),b)
        else :
            temp = "1"+"{:0{}b}".format(abs(int(temp)),b)
        res4.append(temp)
        
        for c in temp :
            res5.append(c)
        

    return res1, res2, res3, res4, res5

def MLT_3(Bit_list):
    x = [i for i in range(len(Bit_list))]
    y = []

    #m pour montant , d pour descendant.
    sens = "m" 
    val = 0

    for el in Bit_list :
        if el == '1' :
            if sens == "m" :
                if val == 1:
                    sens = "d"
                    val = 0
                else :
                    val = 1
            else :
                if val == -1:
                    sens = "m"
                    val = 0
                else :
                    val = -1
        y.append(val)

    return x,y
            
        

#---------------------------------------------
def plot(inx, iny, leg, fmt='-bo', l=""):
    plt.plot(inx,iny,fmt,label=l)
    plt.xlabel('time (s)')
    plt.ylabel('voltage (V)')
    plt.ylim([-5.5, +5.5])

#---------------------------------------------
if __name__ == '__main__':
    np.set_printoptions(linewidth=250) 
    np.set_printoptions(precision=3, suppress=True)
    
    #TEST FOR MSE,SNR AND VAR
    for i in range(1,11):
        a  = 5.0
        b = i
        fe = 2000.0
        f = 50.0
        d = 0.04
        step = 2*a/(2**b)
        
        x,y=tp1.make_sin(a,f,fe,0,d)
        z,err = QS(y,a,b)
        mse = MSE(y,z,fe*d)
        snr = SNR(y,z,fe*d)
        var = variance(y,fe*d)
        print("var=",var,"MSE=",mse,"SNR=",snr)
        
    #############################################
        
    a=5.0
    b=3 #5
    step = 2*a/(2**b)
  
    fe = 2000.0
    f = 50.0
    d = 0.04
    x,y=tp1.make_sin(a,f,fe,0,d)
    #x,y = tp1.make_square(a,f,fe,d)
    #x,y=tp1.make_sintooth(a,f,fe,d)
    
    z,err = QS(y,a,b)
    mse = MSE(y,z,fe*d)
    snr = SNR(y,z,fe*d)

    _,_,_,_,res5 = encodage(y,z,step,b)
    print(encodage(y,z,step,b))

    
    # plot du signal quantifie
    fig = plt.figure(figsize=(12,12))
    ax = fig.add_subplot(1,1,1)

    
    majorLocator = MultipleLocator(step)
    ax.yaxis.set_major_locator(majorLocator) 
    
    plot(x,y,"",'bo', l="Signal")
    plot(x,z,"",'rs', l="Quantized")
    plot(x,err,"",'--x', l="Diff")
    title = "Sinusoide : $f_e={}, f={}, d={}, MSE={}, SNR={}$".format(fe,f,d,mse,snr)
    tp1.decorate_ax(ax,title)
    
    """
    #MANCHESTER
    tp1.decorate_ax(ax,"MANCHESTER SIGNAL")
    plt.step([i for i in range(len(res5))],res5)
    plt.ylim([-0.5, +1.5])
    """

    """
    ########### DERNIER EXO
    tp1.decorate_ax(ax,"MLT-3 SIGNAL")
    x,y = MLT_3(res5)
    plt.step(x,y)
    plt.ylim([-1.5, +1.5])
    """
    
    ###########
    plt.show()    
