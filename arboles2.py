# -*- coding: utf-8 -*-
"""
Created on Sun Aug 16 18:29:24 2020

@author: Administrador
"""

#Ejercicio 3.18
import csv
import os
import matplotlib.pyplot as plt
import numpy as np
            
def leer_arboles(nombre_archivo):
    f=open(nombre_archivo, 'rt', encoding="utf8")
    filas = csv.reader(f)
    encabezado = next(filas)
    arboleda=[]
    for fila in filas:
        record=dict(zip(encabezado,fila))
        arboleda.append(record)
    print (len(arboleda))
    return arboleda
 
nombre_archivo = 'Data/arbolado-en-espacios-verdes.csv'
arboleda =leer_arboles(nombre_archivo)

#Ejercicio 3.19

H=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']

#Ejercicio 3.20

def medidas_de_especies(arboleda):
    medidas =[]
    aux = [[float(arbol['altura_tot']),float(arbol['diametro'])] for arbol in arboleda if arbol['nombre_com'] == 'Jacarandá']
    medidas.append(aux)
    return medidas

medidas=medidas_de_especies(arboleda)

#Ejercicio 4.30: Histograma de altos de Jacarandás
os.path.join('Data','arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
altos=[float(arbol['altura_tot']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
diam=[float(arbol['diametro']) for arbol in arboleda if arbol['nombre_com']=='Jacarandá']
d=np.array(diam)
h=np.array(altos)
plt.hist(altos,bins=50)

#Ejercicio 4.31: Scatterplot (diámetro vs alto) de Jacarandás

plt.scatter(d,h,alpha=0.2)
plt.xlabel("diametro (cm)")
plt.ylabel("alto (m)")
plt.title("Relación diámetro-alto para Jacarandás")
