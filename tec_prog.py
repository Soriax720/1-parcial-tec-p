#Definir una función que retorna la suma de los primeros "i" números naturales
"""n = 10
def suma(n):
    i = 0
    a = 0 #ACUMULADOR
    while i <= n:
        a = a + i
        i = i + 1 #PARA QUE LA CONDICION SE LOGRE
    return a
print(suma(10))
"""
#Def una funcion que retorna el promedio de los primero "i" numeros naturales
"""
def promed(n):
    i = 0
    a = 0
    while i <= n:
        a = a + i
        i = i + 1
    promedio = a / n
    return promedio

print(promed(10))"""
# definir una funcion que calcula la suma de los numeros impares hasta n inclusive
"""def suma_impar(n):
    i = 1
    a = 0
    while i <= n:
        if i % 2 == 1:
            a = a + i

        i = i + 1
    
    return a
print(suma_impar(10))
"""
"""
def inverso(n):
    while n >= 0:
        print(n)
        n = n-1

print(inverso(10))

def raiz_cuadrada(s):
    
    x0 = s / 2
    x1 = 0.5 * (x0 + s/x0)
    x2 = 0.5 * (x1 + s/x1)
    x3 = 0.5 * (x2 + s/x2)
    x4 = 0.5 * (x3 + s/x3)
    return x4

n = raiz_cuadrada(13)
print(n)

def raiz_cuadrada_wh(s):
    i = 10
    x = s / 2
    while i > 0:
        x = 0.5 * (x + s/x)
        i = i - 1
    return x

k = raiz_cuadrada_wh(13)
print(k)   
 while n >= 0:
        print(n)
        n = n-1
"""
"""
v = [3, 5, 6, 7, 10, 12, 13]
def suma(vector):
  i = 0
  acumulador = 0
  ultima = len(vector)-1
  while i <= ultima:
    acumulador = acumulador + vector[i]
    i = i + 1
  return acumulador

def producto(vect):
  acc = 1
  i = 0
  while i <= len(vect)-1:
    acc = acc * vect[i]
    
    i = i + 1
    
  return acc

v = [3, 5, 6, 7, 10, 12, 13]


def media(vector):
  total = suma(vector)
  return total / len(vector)

h = [3,2,1]


def parci(numero, verdad):
  i = 0
  suma = 0
  while i <= numero:
    if verdad == True:
      if i % 2 == 0:
        suma = suma + i

    else: #suma impar
      if i % 2 == 1:
        suma = suma + i
    i = i + 1
 

  
def productoria(n):
 acc = 1
 i = 1
 while i <= n:
    acc = acc * i
    i = i + 1
    
 return acc

print(productoria(5))
"""

#calcular la productoria hasta n con una funcion que retoorne el valor obt.
def productoria(n):
    acum = 1
    i = 1
    while i <= n:
        acum = acum * i
        i = i + 1
    return acum




def ultra_funcion(num,verdad):
    suma = 0
    i = 0
    while i <= num:
        if i % 2 == 0 and verdad == True:
            suma = suma + i
        elif i % 2 == 1 and verdad == False:
              suma = suma + i
        i = i + 1
    return suma

def suma(num1,num2):
    return num1 + num2

def sum_resta(n1,n2):
    if n1 > n2:
        return n1 + n2
    else:
        return n1 - n2
  
def espar(n):
    if n % 2 == 0:
        return True
    return False

def productoria(n):
 acc = 1
 i = 1
 while i <= n:
    acc = acc * i
    i = i + 1
    
 return acc
#####################     VECTORES     ##################
###ejer 1
v = [3, 5, 6, 7, 10, 12, 13]
def suma(vector):
  i = 0
  acumulador = 0
  ultima = len(vector)-1
  while i <= ultima:
    acumulador = acumulador + vector[i]
    i = i + 1
  return acumulador
################ ejer 2################
vector = [1,2,3,22,5,0]
max_ = None
i = 1
while i < len(vector):
   if max_ == None or vector[i] > max_:
      max_ = vector[i]
   i = i + 1




#ejer 2
def producto(vect):
  acc = 1
  i = 0
  while i <= len(vect)-1:
    acc = acc * vect[i]
    
    i = i + 1
    
  return acc

v = [3, 5, 6, 7, 10, 12, 13]

#ejer 4
def media(vector):
  total = suma(vector)
  return total / len(vector)

h = [3,2,1]

##Escribe una función que reciba una lista de números 
# y retorne una nueva lista con los números pares.

#print(len([1,2,3,4,5])-1)
    
def _min(array, desde, hasta):
   if len(array) == 0 or desde > hasta:
      return None
   n = hasta
   i = desde
   while i <= n:
      if i == desde or array[i] < m:
         m = array[i]
         p = i
      i = i + 1
   return p

def sumar(array,desde,hasta):
   if len(array) == 0 or desde > hasta:
      return None
   n = hasta
   i = desde
   a = 0
   while i <= n:
      a += array[i]
      i = i + 1
      return a

def busca1(arr,valor):
    i=0
    n=len(arr)-1
    while i<=n:
        if arr[i] == valor:
            return i
        i+=1
    return -1 
vector = [5,3,8,2,9]
print(busca1(vector,11))

def parsito(vec):
   
   i = 0
   ultimo = len(vec)-1
   cant_pares = 0
   suma_pares = 0
   while i <= ultimo:
      if vec[i] % 2 == 0:
         suma_pares = suma_pares + vec[i]
         cant_pares += 1
      i+= 1
   return suma_pares/cant_pares


##Implementa una función que retorne los primeros N números de la secuencia de 
# Fibonacci.
"""
f0 = 0
f1 = 1
f2 = 1
fn = fn-1 + fn-2

def fibo(f):
   n1 = 0
   n2 = 1
   i = 2
   while i < f:
      n3 = n1 + n2
      n1 = n2
      n2 = n3
      i = i + 1"""
def buscar2(vector, valor): # vector ordenado, sabemos tope (cuando cortar)
    i = 0
    while i <= len(vector)-1 and vector[i] <= valor:
        if vector[i] == valor:
            return i
        i += 1
    return -1

