'''
Created on 19 avr. 2016
@author: menez

Draft !!!!

'''
import socket
from struct import *
import binascii

#====================================================

eth_type = {b'0800' : "IP"}
protocole_type = {1 : "ICMP"
                  ,17 : "UDP"}


def readtrames(filename):
    """
    Cette fonction fabrique une liste de chaines de caracteres a partir du 
    fichier contenant les trames.
    
    Chaque chaine de la liste rendue est une trame du fichier.
    

    return : liste des trames contenues dans le fichier
    """
    file = open(filename)
    trames = [] # List of frames (= trames)
    trame = ""  # Current frame .. string vide
    i = 1
    for line in file : # acces au fichier ligne par ligne
        line = line.rstrip('\n') # on enleve le retour chariot de la ligne
        line = line[6:53]        # on ne garde que les colonnes interessantes  
        print ("lig {} : {}".format(i,line))
        trame = trame + line

        if (len(line) == 0): # Trame separator 
            #print "Ligne vide :", (len(line)) 
            trame = trame.replace(' ','') # on enleve les blancs

            # Faut que la trame contienne un nombre pair de chiffres pour
            # pouvoir etre "unhexlifier" : 2 chiffres hexa => 1 octets
            if (len(trame) % 2) != 0 :
                trame = trame + "0"
            trames.append(trame) # on ajoute la trame a la liste 
            trame = ""       # reset trame
        
        i = i+1
    
    if len(trame) != 0 : # Last frame
        trame = trame.replace(' ','') # on enleve les blancs

        # Faut que la trame contienne un nombre pair de chiffres pour
        # pouvoir etre "unhexlifier" : 2 chiffres hexa => 1 octets
        if (len(trame)%2) != 0 :
            trame = trame + "0"            
        trames.append(trame) # on ajoute la trame a la liste 

    return trames

#====================================================

def decodageEthernet(trame):
    """
    Analyse une trame Ethernet :  cf https://fr.wikipedia.org/wiki/Ethernet    
    Input : trame est une chaine de caracteres

    Je vous donne deux facons d'aborder le probleme !
    """
    print("-"*60)
    print ("\nTrame Ethernet en cours d'analyse : \n{}\n".format(trame))
    raw = trame #On preserve la trame avant de la modifiee.
    print(type(trame))
    trame = binascii.unhexlify(trame) # Les octets representes par cette chaine
    print(type(trame))
    
    # Parse ethernet header
    print ("Header Ethernet :")       
    eth_length = 14 
    eth_header = trame[:eth_length]  # Get the bytes of the header 
    print (type(eth_header))
    
    # Soit on recupere les adresses MAC en UTILISANT le slicing Python.
    mac_dest = eth_header[0:6]
    mac_src = eth_header[6:12]
    print ('Destination MAC : {}'.format(binascii.hexlify(mac_dest)))
    print ('Source MAC \t: {}'.format(binascii.hexlify(mac_src)))

    # Soit on recupere les adresses MAC en UTILISANT unpack
    # For more information on format strings and endiannes, refer to
    # https://docs.python.org/3.5/library/struct.html
    ethfields = unpack('!6s6sH' , eth_header) 
    mac_dest = ethfields[0]
    mac_src = ethfields[1]
    print ('Destination MAC : {}'.format(binascii.hexlify(mac_dest)))
    print ('Source MAC \t: {}'.format(binascii.hexlify(mac_src)))

    
    # Maintenant il faut analyser la suite de la trame  !!!
    #
    #
    Type = eth_header[12:] #Champ type du header ethernet
    print('Type : {} = {}'.format(binascii.hexlify(Type),eth_type[binascii.hexlify(Type)]))

    if eth_type[binascii.hexlify(Type)] == "IP":
        lenraw = raw[eth_length*2:eth_length*2+2] #champ taille du header du protocole ip
        ip_header_len = int(lenraw[0]) * int(lenraw[1])#calcul de la taille du header.
        
        decodageIP(trame[eth_length:],ip_header_len)


def decodageIP(trame, end):
    print('\n--- Decodage IP ---')
    ip_dest = trame[end-4:end]
    ip_source = trame[end-8:end-4]

    protocole = trame[end-11]
    print('Destination logique : {}'.format(binascii.hexlify(ip_dest)))
    print("soit : {}.{}.{}.{}\n".format(trame[end-4],trame[end-3],trame[end-2],trame[end-1]))
    
    print('Source logique : {}'.format(binascii.hexlify(ip_source)))
    print("soit : {}.{}.{}.{}\n".format(trame[end-8],trame[end-7],trame[end-6],trame[end-5]))

    print("Protocole : {}".format(protocole_type[protocole]))

    port_source = trame[end:end+2] #champ port de UDP
    port_dest = trame[end+2:end+4]
    
    lg_udp = trame[end+4:end+6] #champ longueur de UDP
    checksum = trame[end+6:end+8] #champ checksum de UDP
    print("Port source = {}\nPort destination = {}".format(decode_hexa(port_source),decode_hexa(port_dest)))
    print("Longeur = {}\nChecksum = {}".format(decode_hexa(lg_udp),decode_hexa(checksum)))
    
    print("\nData = {}".format(trame[end+8:].decode()))#end+8 pour enlever le header de UDP

    
def decode_hexa(n):
    res = ""
    res += str(int(n[0]) * 256 + int(n[1]))

    return res;

#=================================================================

if __name__ == '__main__':

    filename = "XXX.txt"
    #filename = "ping_req.txt"
    #filename = "dhcp_req.txt"
    #filename = "httpbin_org.txt"
    # Transformation des echanges contenus dans le fichier
    # vers une liste de strings :  une string = une trame
    print("="*60)
    trames = readtrames(filename)

    print("="*60)
    print("\nTrames obtenues :\n")
    for i,t in enumerate(trames):
        print("trame #{} : {}".format(i,t))

    # Analyse de chaque trame de la liste
    for trame in trames:
        decodageEthernet(trame)        

