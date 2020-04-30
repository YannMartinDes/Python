'''
File : write_a_wave.py
@author: menez
'''

import struct, wave, math
import tp1 as tp1_0
import matplotlib.pyplot as plt

#---------------------------------------

def write_a_wave_file(x,y,fn="son.wav"):
    """
    Ecriture d'un signal audio (x,y) dans un fichier audio au format 
    WAV (PCM 8 bits stereo 44100 Hz)

    IL Y A DES CONTRAINTES sur le signal !
    fe = 44100
    Amplitude  <=1
    """
    nbCanal = 2    # stereo
    nbOctet = 1    # taille d'un echantillon : 1 octet = 8 bits
    fe = 44100   # frequence d'echantillonnage
    nbEchantillon = len(x) # nombre d'echantillons
    
    wave_file = wave.open(fn,'w') 
    parametres = (nbCanal,nbOctet,fe,nbEchantillon,'NONE','not compressed') # tuple
    wave_file.setparams(parametres)    # creation de l'en-tete (44 octets)
    
    # niveau max dans l'onde positive : +1 -> 255 (0xFF)
    # niveau max dans l'onde negative : -1 ->   0 (0x00)
    # niveau sonore nul :                0 -> 127.5 (0x80 en valeur arrondi)

    print("La sinusoide devient un son ... ")
    for i in range(0,nbEchantillon):
        val = y[i]
        if val > 1.0:
            val = 1.0
        elif val < -1.0:
            val = -1.0
            
        val = int(127.5 + 127.5 * val)
        try:
            fr  = struct.pack('BB', val,val) # unsigned int      
        except struct.error as err:
            print(err)
            print("Sample {}  = {}/{}".format(i,y[i],val))
                        
        wave_file.writeframes(fr) # ecriture de la frame
        
    wave_file.close()

#---------------------------------------
    
def make_anoisysignal(a,f,fe,ph,d):

    x1,y1 = tp1_0.make_sin(a,f,fe,ph,d)

    m = 0.0 # mean
    e = 0.05 # ecart type
    x2,y2 = tp1_0.noise_white(x1, m, e)

    m1 = 0.0 # mean
    e1 = 1.6*a # ecart type
    x3,y3 = tp1_0.noise_impulse(2, 1000, x1, m1, e1)

    x4,y4 = tp1_0.signal_add(x1,y1,x2,y2)
    x4,y4 = tp1_0.signal_add(x4,y4,x3,y3)

    fig,ax = plt.subplots(1)
    tp1_0.plot_on_ax(ax,x4,y4,"s1 bruite",'r.-')
    tp1_0.decorate_ax(ax,"")
    plt.show()
    
    return x4,y4

#=======================================

if __name__ == '__main__':


    # Generation du signal
    x,y = make_anoisysignal(a=0.2,f=440.0,fe=44100.0,ph=0,d=5)

    write_a_wave_file(x,y)
