
"""Guarde en lista `naturales` los primeros 100 números naturales (desde el 1) 
usando el bucle while
"""
n=1
naturales=[]
while n<=100:
  naturales.append(n)
  n +=1
#print(naturales)



"""Guarde en `acumulado` una lista con el siguiente patrón:

['1','1 2','1 2 3','1 2 3 4','1 2 3 4 5',...,'...47 48 49 50']

Hasta el número 50.
"""
n=1
n2=1
acumulado=[]
temp=[]
while n2<=50:
  while n<=n2:
    temp.append(str(n))
    n +=1
  acumulado.append(" ".join(temp))
  n2 +=1
#print(acumulado)



"""Guarde en `suma100` el entero de la suma de todos los números entre 1 y 100:
"""
n=1
suma100=0
while n<=100:
  suma100 = suma100 + n
  n +=1
#print(suma100)




"""Guarde en `tabla100` un string con los primeros 10 múltiplos del número 134, 
separados por coma, así:

'134,268,...'

"""
n=1
temp=134
tabla100=""
while n<=10:
  if tabla100 == "":
    tabla100 = str(temp)  
  else:
    tabla100 = tabla100 + ',' + str(temp*n)
  n +=1
#print(tabla100)




"""Guardar en `multiplos3` la cantidad de números que son múltiplos de 3 y 
menores o iguales a 300 en la lista `lista1` que se define a continuación (la lista 
está ordenada).
"""
lista1 = [12, 15, 20, 27, 32, 39, 42, 48, 55, 66, 75, 82, 89, 91, 93, 105, 123, 132, 150, 180, 201, 203, 231, 250, 260, 267, 300, 304, 310, 312, 321, 326]

multiplos3=0
for i in lista1:
  if i%3 == 0 and i<300:
    multiplos3 +=1
#print(multiplos3)

"""Guardar en `regresivo50` una lista con la cuenta regresiva desde el número 
50 hasta el 1, así:

[
  '50 49 48 47...',
  '49 48 47 46...',
  ...
  '5 4 3 2 1',
  '4 3 2 1',
  '3 2 1',
  '2 1',
  '1'
]
"""
regresivo50=[]
for i in range(50,0,-1):
  temp=[]
  for e in range(i,0,-1):
    temp.append(str(e))
  regresivo50.append(" ".join(temp))    
#print(regresivo50)




"""Invierta la siguiente lista usando el bucle for y guarde el resultado en 
`invertido` (sin hacer uso de la función `reversed` ni del método `reverse`)
"""
lista2 = list(range(1, 70, 5))
invertido=[]
for i in lista2:
  invertido.insert(0,i)
#print(invertido)




"""Guardar en `primos` una lista con todos los números primos desde el 37 al 300
Nota: Un número primo es un número entero que no se puede calcular multiplicando 
otros números enteros.
"""
n=37
temp=0
fact=0
primos=[]
while n <= 300:
  temp = n-1
  fact = temp  
  for i in range(temp,1,-1):
    fact=fact*(i-1)
  fact = (fact+1)%n
  if fact ==0:    
    primos.append(n)
  #print("numero", n ,"Factorial",temp, " es ", fact)
  n +=1
#print(primos)




"""Guardar en `fibonacci` una lista con los primeros 60 términos de la serie de 
Fibonacci.
Nota: En la serie de Fibonacci, los 2 primeros términos son 0 y 1, y a partir 
del segundo cada uno se calcula sumando los dos anteriores términos de la serie.

[0, 1, 1, 2, 3, 5, 8, ...]

"""
n=2
fibonacci=[0,1]
while n < 60:
  valor=0
  cont=1
  for i in fibonacci[::-1]:
    print(i)
    if cont<=2:
      valor=valor+i
      cont += 1
    else:
      print("sale")
      break
  fibonacci.append(valor)
  print(valor)
  n +=1
#print(fibonacci)


"""Guardar en `factorial` el factorial de 30
El factorial (símbolo:!) Significa multiplicar todos los números enteros desde
el 1 hasta el número elegido.

Por ejemplo, el factorial de 5 se calcula así:

5! = 5 × 4 × 3 × 2 × 1 = 120
"""
factorial=30
for i in range(factorial,1,-1):
    factorial=factorial*(i-1)
#print(factorial)



"""Guarde en lista `pares` los elementos de la siguiente lista que esten 
presentes en posiciones pares, pero solo hasta la posición 80.
"""

lista3 = [941, 149, 672, 208, 99, 562, 749, 947, 251, 750, 889, 596, 836, 742, 512, 19, 674, 142, 272, 773, 859, 598, 898, 930, 119, 107, 798, 447, 348, 402, 33, 678, 460, 144, 168, 290, 929, 254, 233, 563, 48, 249, 890, 871, 484, 265, 831, 694, 366, 499, 271, 123, 870, 986, 449, 894, 347, 346, 519, 969, 242, 57, 985, 250, 490, 93, 999, 373, 355, 466, 416, 937, 214, 707, 834, 126, 698, 268, 217, 406, 334, 285, 429, 130, 393, 396, 936, 572, 688, 765, 404, 970, 159, 98, 545, 412, 629, 361, 70, 602]

pares=[]
posicion =0
for i in lista3:
  if posicion%2 == 0 and posicion <= 80:
    pares.append(i)
  posicion += 1
#print(pares)
#enumerate evita crear la variable posicion


"""Guarde en lista `cubos` el cubo (potencia elevada a la 3) de los números del 
1 al 100. 
"""
n=1
cubos=[]
while n <= 100:
  i=1
  cubo=n
  while i < 3:
    cubo = cubo*n
    i += 1
  cubos.append(cubo)
  n += 1
#print(cubos)




"""Encuentre la suma de la serie 2 +22 + 222 + 2222 + .. hasta sumar 10 términos 
y guardar resultado en variable `suma_2s` 
"""
n= 1
i= 1
serie = '2'
suma_2s=0
while n <= 10:
  while i < n:
    serie = serie + '2'
    i+=1
  suma_2s = suma_2s + int(serie)
  n += 1
#print(suma_2s)
  


"""Guardar en un string llamado `patron` el siguiente patrón llegando a una 
cantidad máxima de asteriscos de 30. 
*
**
***
****
*****
******
*******
********
*********
********
*******
******
*****
****
***
**
*
"""
n= 1
i= 1
serie = '*'
asc=""
des=""
patron = ""
while n <= 30:
  while i < n:
    serie = serie + '*'
    i+=1
  if asc=="":
    asc=serie
  else:  
    asc=asc + '\n' + serie
  
  if des=="" and n!=30:
    des=serie
  elif des!="" and n!=30:
    des=serie + '\n' + des
  else:
    break
  n += 1
#print("asc")  
#print(asc)
#print("des")
#print(des)
patron=asc+'\n'+des
#print(patron)