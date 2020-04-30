import tp1 as tp1_0
import matplotlib.pyplot as plt

#A remplir . . . .

#=======================================

if __name__ == '__main__' :
    a = 2
    f = 50.0
    fe = 1000.0
    ph = 0
    d = 0.08

    x1,y1 = tp1_0.make_sin(a,f,fe,ph,d)
    
    m = 0.0 # mean
    e = 0.2 # ecart type
    x2,y2 = tp1_0.noise_white(x1,m,e)
    
    m1 = 0.0 # mean
    e1 = 2*a # ecart type
    nbi = 2 # nombre d’impulsions sur le signal
    di = 2 # duree d’une impulsion en sample
    x3,y3 = tp1_0.noise_impulse(nbi,di,x1,m1,e1)
    
    x4,y4 = tp1_0.signal_add(x1,y1,x2,y2)
    x4,y4 = tp1_0.signal_add(x4,y4,x3,y3)
    
    fig,ax = plt.subplots(4)
    
    tp1_0.plot_on_ax(ax[0],x1,y1,"s1: {} Hz, {} V".format(f,a),'bo-')
    tp1_0.decorate_ax(ax[0],"")
    
    tp1_0.plot_on_ax(ax[1],x2,y2,"Bruit blanc: Moyenne {}, Ecart Type {}".format(m,e),'g.-')
    tp1_0.decorate_ax(ax[1],"")
    
    tp1_0.plot_on_ax(ax[2],x3,y3,"Bruit impulsif: Moyenne {}, Ecart Type {}".format(m1,e1),'g.-')
    tp1_0.decorate_ax(ax[2],"")
    
    tp1_0.plot_on_ax(ax[3],x4,y4,"s1 bruite",'r.-')
    tp1_0.decorate_ax(ax[3],"")
    
    plt.savefig("./noises_on_sin.png")
    plt.show()

