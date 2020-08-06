#   Ejercicio 1.29 Traductor (rústico) al lenguaje inclusivo

frase = 'Los hermanos sean unidos porque ésa es la ley primera'
palabras = frase.split()
frase_l=[]

for palabra in palabras:
        cad=list(palabra)
        if cad[-1] == 'o':
            cad[-1]= 'e'
        if cad[-2]== 'o':
            cad[-2]= 'e'
        palabra = ''.join(cad)
        frase_l.append(palabra)

frase_t=' '.join(frase_l)
print(frase_t)


# Con la frase. "Todos, tu también" no funciona, ya que la 'o' no se encuentra ni en la última
# ni en la anteúltima

