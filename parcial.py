


def inverNatural(m,n):
    i = 0
    if m > n:
        while m >= 0:
            print(m)
            m = m - 1
    else:
        while i <= n:
            print(i)
            i = i + 1
#print(inverNatural(1,5))



def funcion2(numero, verdad):
    i = 0
    suma = 0
    while i <= numero:
        if verdad:
            if i % 2 == 0:
                suma = suma + i
        else:
            if i % 2 == 1:
                suma = suma +  i
        i = i +  1
    return suma

print(funcion2(5, True)) 





def promedio(n):
    i = 0
    suma = 0
    while i <= n:
        suma = suma + i
        i = i + 1
    return suma / n
#print(promedio(5))





