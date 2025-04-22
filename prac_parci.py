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

def numeros(n1,n2):
    if n1 > n2:
        return n1
    elif n2 > n1:
        return n2
    else:
        print("Son iguales")
    

def calc_perimetro(radio):
    return 2 * 3.14159 * radio

def numeros(n):
    ac= 0
    i = 0
    while i <= n:
        if i % 2 == 1:
            ac = ac + i
        i = i + 1
    return ac


def num_inv(n):
    while n >= 0:
        print(n)
        n = n - 1

#print(num_inv(4))

def sumarTres():
    n1 = int(input("Ingresa un numero: "))
    n2 = int(input("Ingresa otro numero: "))
    n3 = int(input("Ingresa el ultimo numero: "))
    return n1 + n2 + n3

#print(sumarTres())

def saludar():
    name = input("Ingrese su nombre: ")
    print(f'Hola {name} ,como estas?')

#print(saludar())

def pesosADolares(biyuya):
    cambio = 0.00088
    conversion = biyuya * cambio
    return conversion

#print(pesosADolares(10000))

#VolumenCubo: Escribir un programa que pida por teclado la longitud de una arista de
#un cubo, calcule el volumen del cubo y muestre por pantalla el resultado.

def volumenCubo(longitud):
    volumen_cub = longitud**3
    return volumen_cub

#print(volumenCubo(10))

def sumaMultipicacion(n1,n2):
    suma = n1 + n2
    multiplicacion = n1 * n2
    return suma, multiplicacion
#print(sumaMultipicacion(5,2))

def promedioExamenes(nota1,nota2,nota3):
    nota_total = nota1 + nota2 + nota3
    prom = nota_total / 3
    return prom

#print(promedioExamenes(8,6,10))

def perimetroCircuferencia(radio_circuferencia):
    PI = 3.14159
    perimetro = 2 * PI * radio_circuferencia
    return perimetro

#print(perimetroCircuferencia(5))

def anteriorPosterior(numero):
    print(numero)
    ant = numero - 1
    post = numero + 1
    return ant, post

#print(anteriorPosterior(10))

"""Escribir un programa que pida por teclado una hora en horas, minutos
y segundos (datos enteros) y calcule cu´antos segundos han pasado desde las 00:00:00
horas. Luego debe mostrar por pantalla el resultado (entero).
"""

def segundoHoras():
    hora = int(input("Ingrese la hora: "))
    minuto = int(input("Ingrese los minutos: "))
    segundos = int(input("Ingrese los segundos: "))
    hora = hora * 3600
    minuto = minuto * 60
    pasaron = hora + minuto + segundos
    return print(f"Desde las 00:00 pasaron {pasaron} segundos")

#print(segundoHoras())

def sonIguales(n1,n2):
    if n1 == n2:
        print("los numeros son iguales")
    else:
        print("Los numeros son distintos")

#print(sonIguales(5,4))

def queSigno(numero):
    if numero >= 0:
        print("El numero es positivo")
    elif numero < 0:
        print("El numero es Negativo")

#print(queSigno(-10))

"""Ordenar: Escribir un programa que pida dos numeros y los muestre 
por pantalla ordenados de mayor a menor.
"""
def ordenar(num1,num2):
    if num1 > num2:
        print(num1,num2)
    else:
        print(num2,num1)

#print(ordenar(5,10))

"""CantCifras: Escribir un programa que pida un n´umero entre 0 y 9.999 y muestre por
pantalla cuantas cifras tiene."""
def cantCifras(numero):
    if numero <= 9:
        print("Tiene 1 cifra")
    elif numero <= 99:
        print("El numero tiene 2 cifra")
    elif numero <= 999:
        print("El numero tiene 3 cifras")
    elif numero <= 9999:
        print("El numero tiene 4 cifras")

#print(cantCifras(555))

def parImpar(num):
    if num % 2 == 0:
        print("es par")
    elif num % 2 == 1:
        print("Es impar")

#print(parImpar(5))

########    BUCLES  #############
"""def calificacionSegunNota():
    nota = int(input("Ingresar nota: "))
    while nota <= 0 or nota >= 10:
        print("ERROR: Nota incorrecta, debe ser >= 0 y <= 10")"""

def mitadDeNumero():
    num = int(input("Ingresar numero: "))
    cant_dif_0 = 0
    while num != 0:
        mitad = num / 2
        print(f"la mitad de {num} es {mitad}")
        cant_dif_0 = cant_dif_0 + 1
        num = int(input("Ingresar otra vez: "))
    return cant_dif_0
#print(mitadDeNumero())
"""
num_intr = int(input("Ingresar numero: "))
des_user = input("Desea ingrasar otro numero,Si(s) o No(n): ")
num_intr_user = 1
suma = num_intr
while des_user == "s":
    otro_num = int(input("Ingresar numero: "))
    suma = suma + otro_num
    num_intr_user = num_intr_user + 1 
    des_user = input("Desea ingrasar otro numero,Si(s) o No(n): ")"""


#########    FUNCIONES ###########

def mostrar(n):
    i = 1 
    while i <= n:
        print("Modulo ejecutandose")
        i = i + 1

#print(mostrar(5))

def cualMax(n1,n2):
    















    