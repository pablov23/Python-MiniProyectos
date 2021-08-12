# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 23:17:56 2020

@author: Administrador
"""

import random
import numpy as np

#Ejercicio 4.15: Crear
def crear_album(figus_total):
    albumVacio=np.zeros(figus_total, dtype=int)
    return albumVacio

#Ejercicio 4.16: Incompleto
def album_incompleto(A):
    if min(A)==0:
        return True
    else:
        return False
    
#Ejercicio 4.17: Comprar
def comprar_figu(figus_total):
    return random.randint(1,figus_total) 

#Ejercicio 4.18: Cantidad de compras
def cuantas_figus(figus_total):
    cont=0
    nuevoAlbum=crear_album(figus_total)
    while album_incompleto(nuevoAlbum):
        nuevoAlbum[comprar_figu(figus_total)-1]+=1
        cont+=1
    return cont
 
#Ejercicio 4.19:      
a=crear_album(1)
print(album_incompleto(a))
print(comprar_figu(100))
print(cuantas_figus(100))
listaDe6=[cuantas_figus(figus_total=6) for i in range(1000)]
promedio6= np.mean(listaDe6)
print(promedio6)

#Ejercicio 4.20:  
#lista=[cuantas_figus(figus_total=670) for i in range(100)]
#promedio=np.mean(lista)
#print(promedio)