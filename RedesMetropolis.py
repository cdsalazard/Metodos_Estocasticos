import random as rm
import matplotlib as plt
import math as mt
import numpy as np

def dist (h):
    y = mt.exp(-cita*h)
    return y


def hamiltoniano (S,D):
    h = 0.5*(tetha*S-omega*D)
    return h

def sumaS (longitud, lista):
    b = 0
    for a in lista:
        b = b + a
    return b


"""En la siguiente función estamos definiendo como se conecta la red"""      
def sumaSS (longitud, lista):
    b = 0
    s = 0
    for i in range(Nodos):
        a = lista[i]
        for j in range (Nodos):
            if j > i and j <= i+3:
                b = lista[j]
                s = s + a*b                      
    return s


def probabilidad(H):
    p = mt.exp(-1*cita*H)
    return p



t = 400000
Nodos = 38
"yn = dist(xn)"

omega = 3

sigma = 0.4
tetha = 12
cita = 1
estados = []
Hlista =[]
"""Definimos los estados de los nodos aleatoriamente"""

for i in range (Nodos):
     r = np.random.rand()
     if r > 0.5:
         estados.append(1)
     else:
         estados.append(0)

S = sumaS(Nodos,estados)
SS = sumaSS(Nodos, estados)
H = hamiltoniano(S,SS)
Pt = probabilidad (H)

"Hacemos el flip y calculamos la probabildad del cambio y lo comparamos con el número aleatorio"
for i in range (t):
       
    rint = rm.randint(0,Nodos-1)
    if estados[rint] == 1:
        estados[rint] = 0
    else:
        estados[rint] = 1
    
    Sn = sumaS(Nodos,estados)
    SSn = sumaSS(Nodos, estados)
    Hn = hamiltoniano(Sn,SSn)
    dPt = probabilidad (Hn - H)
    rr = np.random.rand()
    if dPt < rr: 
        if estados[rint] == 1:
            estados[rint] = 0
        else:
            estados[rint] = 1
    else:
        S = Sn
        SS = SSn
        H = Hn
        
    if i%120 == 0:
        for v in range(Nodos):
            rrr = np.random.rand()
            if rrr > 0.5 :
                estados[v] = 1
            else:
                estados[v]= 0
            S = sumaS(Nodos,estados)
            SS = sumaSS(Nodos, estados)
            H = hamiltoniano(S,SS)
    Hlista.append(H)
  
"""print(Hlista)"""
    
plt.style.use('fivethirtyeight')
plt.pyplot.hist(Hlista, bins =50)
        
            

