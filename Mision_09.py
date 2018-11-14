#Autora : Mariana Caballero Cabrera

#Programa con ejercicios de listas


#Función que recibe como parámetro una lista de números enteros y regresa UNA NUEVA lista que contiene solo los valores pares de la lista original
def extraerPares (lista):
    nuevaLista =[]
    for dato in lista:
        if dato%2==0:
            nuevaLista.append(dato)
    return nuevaLista


#Función que recibe como parámetro una lista y regresa una nueva lista, con los valores que son mayores a un elemento previo
def extraerMayoresPrevio (lista):
    listaNueva = []
    for dato in range (1,len(lista)):
        if lista[dato]>lista[dato-1]:
            listaNueva.append(lista[dato])
    return listaNueva


#Función  que recibe una lista de valores y regresa una nueva lista con cada pareja de datos intercambiada
def intercambiarParejas(lista):
    nueva=[]

    for k in range(-1,len(lista),2):
        if k >= 1:
            nueva.append(lista[k])
            nueva.append(lista[k-1])


    if len(lista%2)!= 0 :
        nueva.append(lista[len(lista)-1])


    return nueva


#Función , que recibe una lista de valores e intercambia el valor menor y mayor.
def intercambiarMM(lista):
    maximoDato= max(lista)
    minimoDato= min(lista)
    for k in range(len(lista) - 1):
        if lista[k] == minimoDato:
            lista[k]=maximoDato
        elif lista[k] == maximoDato:
            lista[k]=minimoDato
    return lista


#Función que recibe una lista de valores enteros y regresa el promedio 'centro' de los valores. El promedio 'centro' se define como el promedio entero de la lista sin considerar el mayor y el menor de los datos. Si hay más de un mayor/menor solo se descarta uno.
def promediarCentro(lista):
    nuevaLista = lista
    nuevaLista.sort()
    a = nuevaLista[1:len(lista)-1]
    if len(a) > 0:
        promedio = sum(a)//len(a)
        return promedio
    else:
        return 0


#Función que recibe una lista de números y regresa una dupla con la media y la desviación estándar
def calcularEstadistica(lista):
    if len(lista)<=1:
        return 0,0

    acumulador=0
    for dato in lista:
        acumulador += dato
    mean= acumulador/len(lista)

    acumulador2=0
    for dato in lista:
        suma=(dato-mean)**2
        acumulador2=acumulador2+suma
    deviation=((acumulador2)/(len(lista)-1))**(1/2)
    return(mean,deviation)


# Función que recibe como parámetro una lista y regresa la suma de los valores de la lista. Considere que en la suma participan todos los números, excepto los que están al lado de un número 13
def calcularSuma(lista):
    a = lista.copy()
    if 13 not in a:
        return sum(a)
    else:
        for k in range(len(a)):
            if a[k] == 13:
                if k != 0:
                    a[k-1] = False
                a[k] = False
                if k != len(a):
                    a[k+1] = False
        while False in a:
            a.remove(False)
        return sum(a)
