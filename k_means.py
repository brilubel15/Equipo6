from scipy.spatial import distance
#from sklearn.cluster import KMeans
import numpy as np
import random

def distancia(lista1,lista2):
    distancia = distance.euclidean(lista1, lista2)
    return distancia

def centros(lista):
    # Create an empty list for the new centers
    centros_list = []

    # Convert the list into a numpy array
    listasnonpy = np.array(lista)

    for i in listasnonpy:
        centros_list.append(np.mean(listasnonpy,axis = 0))
    return centros_list

def cercanos(puntos,centros):
    lista=[[]for x in centros]
    for i, punto in enumerate(puntos):
        dist=[]
        for j, centro in enumerate(centros):
            dist.append(distancia(punto,centro))
        min=np.argmin(dist)
        lista[min].append(punto)
    return lista

def k_means(puntos):
    # Set an empty list for centers
    k_lista = []

    # Search for the minimum and maximum value in the lists of puntos
    min = puntos[0][0]
    max = min
    for lista in puntos:
        for i in lista:
            temp = i
            if(temp<min):
                min = temp
            elif(temp>max):
                max = temp

    # Define the quantity of ceners according to the quantity of data
    length = 0
    for lista in puntos:
        length+=len(lista)
    if length>3:
        n = random.randint(2, (len(puntos)+1)/3)
    else:
        n = random.randint(2, 3)

    # Create n of centers between the minimum and maximum value in puntos
    for i in range(2, n):
        k_lista.append(random.randint(min, max))

    # Redifine puntos and centers adjusting with the methods cercanos() and centros()
    for i in range(100):
        import pdb; pdb.set_trace()
        k_lista = centros(cercanos(puntos, k_lista))

    # Return the new adjustes list
    return k_lista

def generarPuntos(i, j):
    lista = []
    puntos = []
    j= (int)(j/i)
    for cony in range(i):
        for conx in range(j):
            lista.append(random.randint(0, 100))
        puntos.append(lista)
    return puntos

if __name__ == '__main__':
    puntos = generarPuntos(8, 8)
    print("Antes: ")
    print(puntos)

    k_means(puntos)
    print("Despues: ")
    print(puntos)
