#calculadora usando condicionales y comparacion

print("Esta es la calculadora")

num1 = float(input("Ingrese un numero: "))
num2 = float(input("Ingrese otro numero: "))

operacion = input("que operacion haces? ")
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "/":
    resultado = num1 / num2
elif operacion == "*":
    resultado = num1 * num2
else:
    print("Seleccion incorrecta")
    resultado = "nada"
print("EL resultado es: ", resultado)

#detecta par o impar
num = int(input("ingresar un numero"))
if (num % 2) == 0:
    print("es par")
else: 
    print("no es par")

# a = "=" OPERADOR DE ASIGNACION
# a == "=" OPERADOR DE COMPARACION


#OPERADORES DE COMPARACION 

a = 2
b = 2

a ==b
a >= b
a < b
a <= b
a != b

print(a != b)



#BUCLES  

i = 0
while i < 10:  
    i = i + 1
    print(i)


i= 0
suma = 0
while i < 10:
    suma = suma + i
    i = i + 1
    print (suma)
print ("Fin ciclo")


#Ciclo impares
i= 0
suma = 0
while i < 10:
    if i % 2 == 1:
        suma = suma + i
    i = i + 1
print (suma)
print ("Fin ciclo")

#Ciclo pares
i= 0
suma = 0
while i < 10:
    if i % 2 == 0:
        suma = suma + i
    i = i + 1
print (suma)
print ("Fin ciclo")

## clase 3

#FUNCIONES

def esPar(numero):
    if(numero % 2) == 0:
        return True
    return False
a = 2
b = esPar(a)



def SumnaUno(n):
    return n + 1
c = SumnaUno(9)
print(c) 


def SumnaUno(n):
    return n + 1

def suma (x, y):
    s = x + y
    return s
c = SumnaUno(9)
print(c) 


d = suma (4,5)
g = suma (12311, 123)
h = suma(123213, 12)
print(d)


#EJEMPLO CON  STRING
def imprime (a):
    print(a)

imprime ("hola clase")


def esPar(numero):
    if(numero % 2) == 0:
        return True
    print("Si el numero es par esto no se ejecuta")
    return False
esPar(10)


def Mayor(a,b):
    if a > b:
        return True
    return False

print(Mayor(10,5))

# ALTERNATIVAS
def esMayor(a,b):
    if a > b:
        return True
    return False

num1 = 2
num2 = 1
c = esMayor(num1,num2)
print(c)
###################################
def Suma(num1, num2):
  return num1 + num2

print("Programa")

n1 = input("Ingrese numero")
n1 = int(n1)

n2 = input("Ingrese otro numero")
n2 = int(n2)

print(Suma(n1, n2))

print("FIN")
"""

#INGRESO  MAYO MENOR
"""
def Compa(num1, num2):
    if num1 > num2:
        return True
    return False



n1 = input("Ingrese numero    ")
n1 = int(n1)

n2 = input("Ingrese otro numero   ")
n2 = int(n2)

print("El resultado es  ")
print(Compa(n1, n2))



def AreaC(diametro):
    pi = 3.1416
    radio = diametro / 2
    return radio * radio * pi

a = AreaC(4)
print(a)


def AreaC(diametro):
    pi = 3.1416
    radio = diametro / 2
    return radio * radio * pi


def perimetro(radio):
    pi = 3.1416
    return 2 * radio * pi

a = AreaC (4)
print(a)

p = perimetro(2)
print(p)

def mayor(a,b):
    if a>b :
        return a
    return b

M = mayor (5,6)
print (M)


def mayor(a, b):
    if a > b :
        return a
    return b

def menor (a, b):
    if a < b:
        return a
    return b



#WHILE

print ("Star")
i = 0
while i < 4:
    print ("Ahora  i vale : ", i)
    i = i + 1
print ("Sigue fuera del while")    

#EJEMPLO

n = 10
def suma(n):
    i = 0
    a = 0 #ACUMULADOR
    while i <= n:
        a = a + i
        i = i + 1 #PARA QUE LA CONDICION SE LOGRE
    return a
print(suma(10))

##classe 6
"""
i = 1
acumulador = 0
while i <= 4:
    acumulador = acumulador + i
    i = i + 1
    print(acumulador, i)
print(acumulador)
""""""

def sumar(numero):
    i = 1
    acumulador = 0
    while i <= numero:
        acumulador = acumulador + i
        i = i + 1
    return acumulador

print(sumar(4))
"""
"""
def sumar(numero):
    i = 1
    acumulador = 0
    while i <= numero:
        acumulador = acumulador + i
        i = i + 1
    return acumulador

def promedio(numero):
     return sumar (numero)/ numero
p = promedio (100)
print(p)

"""

"""
#VECTORES

a = 10

v = [3, 5, 6, 7, 10, 12, 13]

uno = v[0] #LLAMADO ESPECIFICO
n = len(v) # LLAMADO TOTAL ARRAY
print(n)
print(len("hola")) #LECTURA CARACTERES
"""
#METODOS DE ORDENAMIENTO DE VECTORES

v = [3, 5, 6, 7, 10, 12, 13]
i = 0
print(v[i]) #asigno variable al vector
u = len(v)-1 #me lleva al ultimo elemento del vector al restar 1
print(v[u]) # imprime el ultimo vector
#####################################################
acumulador = 0
i = 0        #PRIMERA POSICION DEL VECTOR
u = len(v)-1 #ULTIMA POSICION DEL VECTOR

while i <= u:
    print(v[i])    
    acumulador = acumulador + v[i]
    i = i + 1
print(acumulador)

#####################################################
v = [3, 5, 6, 7, 10, 12, 13]
def suma(vector):
    acumulador = 0
    i = 0        #PRIMERA POSICION DEL VECTOR
     
    while i <= len(v)-1: #ULTIMA POSICION DEL VECTOR
        print(v[i])    
        acumulador = acumulador + vector[i]
        i = i + 1
        return acumulador
print(suma(v))

############################
emiliano = [1, 2, 5]
u = len(emiliano)-1
print(emiliano[u])