'''
File : tp1_0_stud.py

Creer un signal numerique et l'afficher

RMQ : On utilise ici le B,A,BA de Python. 

      Mais si vous savez faire mieux : objets ?, numpy ?
      ... SURTOUT lachez vous !!!!!

     car la solution "pythonique" n'est pas là :-( 
'''

import math
import random
import matplotlib.pyplot as plt 
#---------------------------------------

def make_sin(a=1.0, f=440.0, fe=8000.0, ph=0, d=1):
    """
    Create a synthetic 'sine wave'
    """
    omega = 2*math.pi*f
    N = int(d*fe) #Le nombre d'echantillonage
    te = 1.0/fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te*i
        sig_t.append(t)
        sig_s.append(a*math.sin((omega*t)+ph))
        
    return sig_t, sig_s

def make_square(a=1.0, f=440.0, fe=8000.0, d=1):
    """
    Create a synthetic 'square wave'
    """
    omega = 2*math.pi*f
    N = int(d*fe) #Le nombre d'echantillonage
    te = 1.0/fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te*i
        sig_t.append(t)
        sig_s.append(square(t,f,a)) #ou a*sign(math.sin((omega*t)))
        
    return sig_t, sig_s

def make_sintooth(a=1.0, f=440.0, fe=8000.0, d=1):
    """
    Create a synthetic 'sintooth wave'
    """
    omega = 2*math.pi*f
    N = int(d*fe) #Le nombre d'echantillonage
    te = 1.0/fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te*i
        T = 1/f
        sig_t.append(t)
        sig_s.append(2*a*((t/T) - math.floor(t/T) - 0.5)) 
        
    return sig_t, sig_s

def make_triangle(a=1.0, f=440.0, fe=8000.0, d=1):
    """
    Create a synthetic 'triangle wave'
    """
    omega = 2*math.pi*f
    N = int(d*fe) #Le nombre d'echantillonage
    te = 1.0/fe
    
    sig_t = [] 
    sig_s = []
    for i in range(N):
        t = te*i
        T = 1/f
        sig_t.append(t)
        sig_s.append(a*(4*abs(t/T - math.floor(t/T + 0.5))-1)) 
        
    return sig_t, sig_s

def noise_white(x_set,m,e):
    """
    Create a noise of gauss
    """
    sig_t = [] 
    sig_s = []
    for x in x_set:
        sig_t.append(x)
        sig_s.append(random.gauss(m,e))
        
    return sig_t, sig_s


def noise_impulse (nb, d, x, m, e):
    x_ech = [x[random.randint(0, len(x))] for i in range(nb)]

    _y = [m for i in range(len(x))]
    for i in range(len(x)):
        if x[i] in x_ech:
            for k in range(d):
                if i+k < len(x) :
                    _y[i+k] += random.gauss(m, e)
    return x, _y

def signal_add (x, y, a, b):
    ret = []
    for i in range(len(y)):
        ret += [b[i] + y[i]]
    return x, ret

#---------------------------------------

def plot_on_ax(ax, inx, iny, label, format='--g*'): #--g*
    #on ne voit pas bien le trace de la courbe
    ax.plot(inx,iny,format,label=label)
    ax.margins(0.05)
    ax.set_xlabel('time (s)')
    ax.set_ylabel('voltage (V)')

#---------------------------------------

def decorate_ax(ax, title):
    ax.set_title(title)
    ax.grid(True)
    #ax.legend(loc="center right", numpoints = 1) #pour le carre
    ax.legend(loc="lower left", numpoints = 1) #modif de l'ancre et du nombre de point

#=======================================
    
def sign(x):
    if abs(x) < 0.05 :
        return 0
    if x < 0:
        return -1
    return 1

def square(t,f,a):
    return 2*a*(2*math.floor(f*t) - math.floor(2*f*t))+ 1*a

#=======================================

if __name__ == '__main__':

    """
    ################EXO 1]
    
    a=2 # amplitude. (de 0 à 2)
    periode = 0.02 #une periode.
    f=1/periode  #frequence 1/T
    fe=20/periode #frequence echantillonage  (nbdepoint/periode) 
    ph=0 #phase a l'origine.
    #on sais que N = 80, et N = d * fe -> d = N / fe.
    d=80/fe #d la duree

    fig,ax = plt.subplots()

    # Generation du signal
    x,y=make_sin(a,f,fe,ph,d)
    plot_on_ax(ax,x,y,"Sin Wave : a={}, f ={}, fe={}, ph={}, d={}".format(a,f,fe,ph,d),"-bo")
    
    decorate_ax(ax,"une sinusoide") #le titre
    plt.savefig("./basic_sin.png")
    plt.show()
    """

    """
    ###################EXO 1.3]
    
    periode = 0.02 #une periode.
    f=1/periode  #frequence 1/T
    ph=0 #phase a l'origine.
    
    #pour les deux courbes
    fe1 = 10/periode
    d1 = 0.04
    a1 = 1.3

    d2 = d1
    fe2 = 20/periode
    a2 = 0.5
    ph2 = math.pi #on oppose par rotation 180 degre

    #modifiee
    x,y=make_sin(a1,f,fe1,ph,d1)
    #deuxieme courbe
    x2,y2=make_sin(a2,f,fe2,ph2,d2)
    
    # Representation graphique
    fig,ax = plt.subplots()
    
    plot_on_ax(ax,x,y,"s1 : {} Hz, {} V, fe= {} Hz, {} rad, {} s".format(f,a1,fe1,ph,d1),"bo")
    plot_on_ax(ax,x2,y2,"s2 : {} Hz, {} V, fe= {} Hz, {} rad, {} s".format(f,a2,fe2,ph2,d2),"r.")

    decorate_ax(ax,"deux signaux") #le titre

    plt.savefig("./Deux_signaux.png")
    plt.show()
    """

    
    ###############EXO 2
    """
    ###########Carré
    fig,ax = plt.subplots()
    # DANS plot_on_ax :
        #ax.legend(loc="center right", numpoints = 1)
    
    xc,yc = make_square(3,50,800,0.08)
    plot_on_ax(ax,xc,yc,"a=3,f=50,fe=800,d=0.08","-bo")

    # avec 300 la duree des etats n'est pas constante et prend une taille qui s'alterner. La fe est trop faible.
    xs,ys = make_sin(3,50,800,0,0.08) #Pour le sinus afin de voir. 
    plot_on_ax(ax,xs,ys,"","-ro")
    
    decorate_ax(ax,"Carré") #le titre
    plt.savefig("./square_sign.png")
    plt.show()
    """

    """
    ###########Sinthooth
    fig,ax = plt.subplots()
    
    xc,yc = make_sintooth(3,50,800,0.08)
    plot_on_ax(ax,xc,yc,"a=3,f=50,fe=800,d=0.08","-bo")
    decorate_ax(ax,"Sintooth") #le titre
    
    plt.savefig("./sintooth.png") #ce n'est pas en 3 a 0.02 car fe est trop bas. on peut decaler fe pour avoir 3 qui est pris en compte (fe-0.001)
    plt.show()
    """

    
    #############Triangle
    fig,ax = plt.subplots()
    
    xc,yc = make_triangle(3,50,800,0.08)
    plot_on_ax(ax,xc,yc,"a=3,f=50,fe=800,d=0.08","-bo")
    decorate_ax(ax,"triangle") #le titre
    
    plt.savefig("./triangle.png")
    plt.show()
    
    
#=======================================
#III] a) c'est la frequence b) fe* taille en bit d'une valeur c)
