# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 22:26:23 2020

@author: Administrador
"""
import random

valores = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
palos = ['oro', 'copa', 'espada', 'basto']
naipes = [(valor,palo) for valor in valores for palo in palos]

print(random.sample(naipes,k=1))

#Barajo sin reposición
def barajar():
        mano=[]
        carta=(random.sample(naipes,k=1)) 
        mano.append(carta)
        carta=(random.sample(naipes,k=1)) 
        mano.append(carta)
        carta=(random.sample(naipes,k=1)) 
        mano.append(carta)
        
        return mano

def envido(mano):
    
    par = False
    punt = 0
    noSuma =[10,11,12]
    puntc1=0
    puntc2=0
    puntc3=0
    valor1=0
    valor2=0
    
    #Si se cumplen las condiciones de tener al menos dos cartas del mismo palo y las valores de las cartas no son 10, 11 ni 12, se
    #Almacena el valor de la carta en una variable, y se cambia la variable par a True, para luego sumar 20 al puntaje total
         
    if mano[0][0][1] == mano[1][0][1]:
        par = True
        if mano[0][0][0] not in noSuma:
            puntc1=mano[0][0][0]   
        if mano[1][0][0] not in noSuma:
            puntc2=mano[1][0][0]
            
    if mano[0][0][1] == mano[2][0][1]:
        par = True
        if mano[0][0][0] not in noSuma:
            puntc1=mano[0][0][0]
        if mano[2][0][0] not in noSuma:
            puntc3=mano[2][0][0]
          
        
    if mano[2][0][1] == mano[1][0][1]:
        par = True
        if mano[2][0][0] not in noSuma:
            puntc3=mano[2][0][0]       
        if mano[1][0][0] not in noSuma:
            puntc2=mano[1][0][0]
            
    #En el caso de que sean 3 cartas iguales sumo los valores más grandes
    aSumar=[puntc1,puntc2,puntc3]
    valor1=max(aSumar)
    aSumar.pop(aSumar.index(max(aSumar)))
    valor2 = max(aSumar)

    
    punt+=valor1+valor2
    
    #A puntaje le sumo 20 si tuve al menos dos cartas iguales
    if par:
        punt+=20
    return punt
        
#Defino las funciones a utilizar para los 3 valores de envido pedidos

def son33(mano):
    if envido(mano) == 33:
        return True
    else:
        return False
    
def son32(mano):
    if envido(mano) == 32:
        print(mano)
        return True
    else:
        return False
    
def son31(mano):
    if envido(mano) == 31:
        return True
    else:
        return False
    
N =10000

G33 = sum([son33(barajar()) for i in range(N)])
prob33 = G33/N
G32 = sum([son32(barajar()) for i in range(N)])
prob32 = G32/N
G31 = sum([son31(barajar()) for i in range(N)])
prob31 = G31/N

print(f'Dí {N} veces, de las cuales {G33} saqué 33.')
print(f'Podemos estimar la probabilidad de sacar 33 es {prob33:.6f}.')

print(f'Dí {N} veces, de las cuales {G32} saqué 32.')
print(f'Podemos estimar la probabilidad de sacar 32 es {prob32:.6f}.')

print(f'Dí {N} veces, de las cuales {G31} saqué 31.')
print(f'Podemos estimar la probabilidad de sacar 31 es {prob31:.6f}.')