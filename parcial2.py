v = [3, 4, 1, 2, 0, 5, 7]
   #[0, 1, 2, 3, 4, 5, 7]
   #[7, 5, 4, 3, 2, 1, 0]


def buscar_minimo(v, d, h):
  i = d
  j = None
  while i <= h:
    if i == d or v[i] < m:
      j = i
      m = v[i]
    i = i + 1
  return j

  
def ordena(vector):    
  i = 0
  while i <= len(vector)-1:
    p = buscar_minimo(vector,i, len(vector)-1)
    tmp = vector[p]
    vector[p] = vector[i]
    vector[i] = tmp
    i = i + 1
  print(vector)


def busqueda_binaria(vector, num):
  pi = 0
  pd = len(vector)-1

  while pi <= pd:
    medio = (pi + pd) // 2
    if vector[medio] == num:
      return medio
    elif vector[medio] < num:
      pi = medio + 1
    else:
      pd = medio - 1
  return -1

a = [-2, 0, 1, 2 ,3 ,6 , 12, 13, 32]
p = busqueda_binaria(a, 2)



def es_un_palindromo(palabra):
    i = 0
    m = (len(palabra) // 2) - 1

    while i < m:
        if palabra[i] != palabra[len(palabra) - 1 - i]:
            return False
        i = i + 1
    return True

#print(es_un_palindromo(p))

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

def ordenar_burbuja(vector):
    lista = vector[:]
    n = len(lista)
    i = 0
    while i < n:
        j = 0
        while j < n - i - 1:
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            j += 1
        i += 1
    return lista
vector = [-1, 0, 3, 6, 5, 4,-2]
resultado= ordenar_burbuja(vector)

def suma_vectores(v1,v2):
    if len(v1) == len(v2):
        v = []
        i = 0
        while i < len(v1):
            v.append(v1[i] + v2[i])
            i = i + 1
        return v
    else:
        return None

def eliminar_ocu(vector,numero):
    i = 0
    v = []
    while i < len(vector):
        if vector[i] != numero:
            v.append(vector[i])
        i = i + 1
    return v
a = [2,4,5,2]